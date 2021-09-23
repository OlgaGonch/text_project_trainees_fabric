import os

from src.models.implementations.model_factory import ModelFactory
from src.models.implementations.model_training import ModelTrainer

if __name__ == "__main__":
    data_path = os.path.abspath('../data/'+'/')
    factory = ModelFactory()
    factory.add_model('bigARTMsimple', ModelTrainer)
    factory.add_model('bigARTMregularisation', ModelTrainer)
    model = factory.get_instance(name='bigARTMsimple',
                                 data_folder_path='{0}/tmp/text_ready'
                                                  '.txt'.format(data_path),
                                 data_batches_path='{0}/batches/'.format(data_path),
                                 batch_size=100,
                                 num_collection_passes=10,
                                 count_of_terms=10)
    print(type(model))
    model.train_model()
