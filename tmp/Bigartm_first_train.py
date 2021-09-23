import artm

def train(
        self,
        initial_data: str,
        calls_data: str,
        count_of_terms: int,
) -> None:
    """
    Метод тренировки модели BigArtm с формированием словаря

    :param initial_data: путь ко всем текстам для анализа
    :param calls_data: путь к батчам
    :type count_of_terms: количество тем
    """
    self._count_of_terms = count_of_terms

    # формирование батчей
    batch_vectorizer = artm.BatchVectorizer(data_path=initial_data,
                                            data_format="vowpal_wabbit",
                                            target_folder=calls_data,
                                            batch_size=100
                                            )
    # задаем название тем
    topic_names = ["sbj" + str(i) for i in range(count_of_terms)]
    model_artm = artm.ARTM(
        num_topics=count_of_terms,
        topic_names=topic_names,
        class_ids={"text": 1},
        cache_theta=True,
        seed=1)
    dictionary_sc = artm.Dictionary('dictionary')  # объявляем словарь, как объект (по сути его еще нет)
    dictionary_sc.gather(batch_vectorizer.data_path)  # собираем словарь из батчей
    dictionary_sc.filter(min_tf=20, max_tf=50000)  # удаляем из словаря низко и высокочастотные слова

    # добавляем скорринги в модель
    model_artm.scores.add(artm.TopTokensScore(name="top_words", num_tokens=25, class_id="text"))
    model_artm.scores.add(artm.PerplexityScore(name='PerplexityScore'))
    model_artm.scores.add(artm.SparsityPhiScore(name='SparsityPhiScore', class_id="text"))
    model_artm.scores.add(artm.SparsityThetaScore(name='SparsityThetaScore'))
    model_artm.scores.add(artm.TopTokensScore(name="top_words_500", num_tokens=500, class_id="text"))

    # инициализируем словарь
    model_artm.initialize("dictionary")

    # обучаем словарь
    model_artm.fit_offline(batch_vectorizer=batch_vectorizer, num_collection_passes=10)

    print(model_artm.score_tracker["PerplexityScore"].last_value)
    print(model_artm.score_tracker["SparsityPhiScore"].last_value)
    print(model_artm.score_tracker["SparsityThetaScore"].last_value)