from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
# most code taken from TensorFlow tutorial and repurposed for music generation

path_to_file = "dataNotes.txt" #file encoded training data is stored under
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))
# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
checkpoint_dir = './training_checkpointsNotes'
vocab_size = len(vocab)
# The embedding dimension
embedding_dim = 256
# Number of RNN units
rnn_units = 1024

#function to build model, model will be built first before loading weights from checkpoint file
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model


tf.train.latest_checkpoint(checkpoint_dir)#getting most recent checkpoint
print(tf.train.latest_checkpoint(checkpoint_dir))
model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))#loading weights from checkpoint into model
model.build(tf.TensorShape([1, None]))
model.summary()

def generate_text(model, start_string):
  # Evaluation step (generating text using the learned model)
  # Number of characters to generate
  num_generate = 6000

  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # Empty string to store our results
  text_generated = []

  # Low temperatures results in more predictable text.
  # Higher temperatures results in more surprising text.
  # Experiment to find the best setting.

  temperature = 1.0
  #temperature = 1.1
  #temperature = 0.9
  #temperature = 2.0
  #temperature = 0.1
  #temperature = 0.8


  # Here batch size == 1
  model.reset_states()
  for i in range(num_generate):
      predictions = model(input_eval)
      # remove the batch dimension
      predictions = tf.squeeze(predictions, 0)

      # using a categorical distribution to predict the word returned by the model
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # We pass the predicted word as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

generatedNotes= generate_text(model, start_string=u"57 66 72") #generating note values from seed string
print(generatedNotes)
file1 = open("generatedNotes.txt","a") #saving generated notes to text file
file1.write(generatedNotes)
file1.close()

#some old debug code below

# with open("generatedNotes.txt", 'r') as file:
#     outString = file.read()
#
# if outString.strip()== generatedNotes:
#     print("true")
# else:
#     print("false")
#     print(generatedNotes)