import artm

from typing import Any
from ...interface.IModel import IModel


class ModelTrainer(IModel):
    def __init__(self, data_folder_path, data_batches_path, batch_size, num_collection_passes, count_of_terms):
        self.count_of_terms = count_of_terms
        self.data_folder_path = data_folder_path
        self.data_batches_path = data_batches_path
        self.batch_size = batch_size
        self.num_collection_passes = num_collection_passes

    def train_model(self) -> Any:
        print('ok')

        batch_vectorizer = artm.BatchVectorizer(data_path=self.data_folder_path, data_format='vowpal_wabbit',
                                                target_folder=self.data_batches_path, batch_size=self.batch_size)

        topic_names = ['sbj' + str(i) for i in range(self.count_of_terms)]

        model_artm = artm.ARTM(num_topics=self.count_of_terms, topic_names=topic_names, class_ids={'text': 1},
                               cache_theta=True, seed=1)

        model_artm.scores.add(artm.PerplexityScore(name='PerplexityScore', dictionary='dictionary'))
        model_artm.scores.add(artm.SparsityPhiScore(name='SparsityPhiScore', class_id="text"))
        model_artm.scores.add(artm.SparsityThetaScore(name='SparsityThetaScore'))
        model_artm.scores.add(artm.TopTokensScore(name="top_words_100", num_tokens=100, class_id="text"))
        model_artm.scores.add(artm.TopTokensScore(name="top_words_25", num_tokens=25, class_id="text"))

        dictionary_sc = artm.Dictionary('dictionary')
        dictionary_sc.gather(batch_vectorizer.data_path)
        dictionary_sc.filter(min_tf=20, max_tf=50000)

        model_artm.initialize('dictionary')

        model_artm.fit_offline(batch_vectorizer=batch_vectorizer, num_collection_passes=self.num_collection_passes)

        print(model_artm.score_tracker["PerplexityScore"].last_value)
        print(model_artm.score_tracker["SparsityPhiScore"].last_value)
        print(model_artm.score_tracker["SparsityThetaScore"].last_value)

        return model_artm
