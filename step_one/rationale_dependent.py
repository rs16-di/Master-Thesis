#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
rationale_dependent.py

"""
from options import load_arguments
from IO import create_embedding_layer, read_annotations, create_batches
import tensorflow as tf

from models import Model
def main():
    print 'Parser Arguments' 
    for key, value in args.__dict__.iteritems():
        print u'{0}: {1}'.format(key, value)
        
    # ensure embeddings exist
    assert args.embedding, "Pre-trained word embeddings required."
    
    embed_layer = create_embedding_layer(
                                         args.embedding
                                         )
    
    max_len = args.max_len
    
    if args.train:
        train_x, train_y = read_annotations(args.train)
        train_x = [ embed_layer.map_to_ids(x)[:max_len] for x in train_x ]
                   
    # TODO: create development and test sets and rationale stuff
            

    if args.train:
        with tf.Graph().as_default() as g: 
            with tf.Session() as sess:
                # initialize Model
                #TODO: create encoder class in model
                
                model = Model(
                            args = args,
                            embedding_layer = embed_layer,
                            nclasses = len(train_y[0])
                        )
                model.ready()
                
                # added this for testing
                # TODO: Remove later
                model.train((train_x, train_y),None, None, None, sess) 
            
            '''
            train_batches_x, train_batches_y = create_batches(
                                train_x, train_y, args.batch, model.generator.padding_id
                            )
            
            feed_dict={model.generator.x: train_batches_x[0],model.encoder.y : train_batches_y[0], model.generator.embedding_placeholder: embed_layer.params[0], 
                      model.generator.dropout: 0.5, model.generator.training: True}
                      
            
            init = tf.initialize_all_variables()
            
            
            sess.run(init)
            print 'past graph initialization'
            
            
            # cost_g = sess.run(model.encoder.cost_g , feed_dict)
            
            print cost_g
            '''
        
    

def reset_graph():
    if 'sess' in globals() and sess:
        sess.close()
    tf.reset_default_graph()
    
    
if __name__ == '__main__':
    args = load_arguments()
    
    # reset zie graph
    reset_graph()
    
    # start procedures
    main()

