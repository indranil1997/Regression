import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
learning_rate = 0.01
epochs = 200
n_samples = 30
train_x = np.linspace(0,20,n_samples)
train_y = 3*train_x + 4*np.random.randn(n_samples)


X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

w = tf.Variable(np.random.randn(), name = 'Weights')
b = tf.Variable(np.random.randn(), name = 'Bias')

prediction = X*w + b

cost = tf.reduce_sum((prediction - Y)**2)/(2*n_samples)

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
    for epoch in range(epochs):
        for x,y in zip(train_x,train_y):
            sess.run(optimizer, feed_dict={X:x, Y:y})
            
        if not epoch % 20:
            c = sess.run(cost, feed_dict = {X:train_x, Y:train_y})
            W = sess.run(w)
            B = sess.run(b)
            print(f'epoch: {epoch:04d} c={c:.4f} W={W:.4f} B={B:.4f}')
            
            
    weight = sess.run(w)
    bias = sess.run(b)
    plt.plot(train_x, train_y,'x')
    plt.plot(train_x, weight*train_x + bias)
    plt.show()
