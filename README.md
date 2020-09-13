# reframing_quality_estimation

Transformer based model on multimodal quality estimation

## pre_process
generate_visual_features: used resnet50 pre-trained model to extract the visual features.
decoy_images: geneate interference images for label annoation.

## transquest
Transformer based model based on transquest framework. We add the new features of fusing CLS vector representation with the visual features to do the quality estimation.
