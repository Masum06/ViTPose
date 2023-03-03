_base_ = [
    '../../../../_base_/default_runtime.py',
    '../../../../_base_/datasets/hi510k.py'
]

#interval - how often to evaluate the model - set to 1 to evaluate after every epoch
evaluation = dict(interval=1, metric=['PCK', 'AUC', 'EPE'], save_best='AUC')

optimizer = dict(
    type='Adam',
    lr=5e-4,
)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[170, 200])
total_epochs = 400 #Total epochs
log_config = dict(
    interval=10,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])

channel_cfg = dict(
    num_output_channels=21,
    dataset_joints=21,
    dataset_channel=[
        [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20
        ],
    ],
    inference_channel=[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20
    ])

# model settings
model = dict(
    type='TopDown',
    pretrained='torchvision://resnet50',
    backbone=dict(type='ResNet', depth=50, num_stages=4, out_indices=(3, )),
    neck=dict(type='GlobalAveragePooling'),
    keypoint_head=dict(
        type='DeepposeRegressionHead',
        in_channels=2048,
        num_joints=channel_cfg['num_output_channels'],
        loss_keypoint=dict(type='SmoothL1Loss', use_target_weight=True)),
    train_cfg=dict(),
    test_cfg=dict(
        flip_test=True,
        post_process='default',
        shift_heatmap=True,
        modulate_kernel=11))

data_cfg = dict(
    image_size=[256, 256],
    heatmap_size=[64, 64],
    num_output_channels=channel_cfg['num_output_channels'],
    num_joints=channel_cfg['dataset_joints'],
    dataset_channel=channel_cfg['dataset_channel'],
    inference_channel=channel_cfg['inference_channel'])

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='TopDownRandomFlip', flip_prob=0.5),
    dict(
        type='TopDownGetRandomScaleRotation', rot_factor=90, scale_factor=0.3),
    dict(type='TopDownAffine'),
    dict(type='ToTensor'),
    dict(
        type='NormalizeTensor',
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]),
    dict(type='TopDownGenerateTargetRegression'),
    dict(
        type='Collect',
        keys=['img', 'target', 'target_weight'],
        meta_keys=[
            'image_file', 'joints_3d', 'joints_3d_visible', 'center', 'scale',
            'rotation', 'flip_pairs'
        ]),
]

val_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='TopDownAffine'),
    dict(type='ToTensor'),
    dict(
        type='NormalizeTensor',
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]),
    dict(
        type='Collect',
        keys=['img'],
        meta_keys=['image_file', 'center', 'scale', 'rotation', 'flip_pairs']),
]

test_pipeline = val_pipeline



#TODO: @cengiz, change this to the correct path
data_root = '/media/hci-monster-linux/PARK_HANDS1/Hand Dataset/hi5_500k' #annotations folder (should be like: /home/hci-monster-linux/Park_Hands/HandDatsetor something) the Annotations/file is below in ann_file
train_img_root = '/media/hci-monster-linux/PARK_HANDS1/Hand Dataset/hi5_500k/train' #image folder (should be like: /home/hci-monster-linux/Park_Hands/HandDatset/Images/400k/train or something)

"""
Changed val/test data to OneHand10K dataw
"""

one_hand_data_root = '/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/onehand10k'
test_img_root = '/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/onehand10k/Test/source'
val_img_root = test_img_root



data = dict(
    samples_per_gpu=16, #reduced from 64
    workers_per_gpu=2,
    val_dataloader=dict(samples_per_gpu=8), #reduced from 32
    test_dataloader=dict(samples_per_gpu=8), #reduced from 32
    train=dict(
        type='Hi510KDataset',
        # data/hi5_50K/50K Dataset/data/annotations/
        ann_file=f'{data_root}/annotations/hi5_500k_train.json', #TODO: @cengiz, change this to the correct path Annotations/500K/train_json
        img_prefix=f'{train_img_root}/',
        data_cfg=data_cfg,
        pipeline=train_pipeline,
        dataset_info={{_base_.dataset_info}}),
    #val is now just the test set instead of its own validation set
    val=dict(
        type='OneHand10KDataset',
        ann_file=f'{one_hand_data_root}/annotations/onehand10k_test.json', #onehand test set 
        img_prefix=f'{val_img_root}/',
        data_cfg=data_cfg,
        pipeline=val_pipeline,
        dataset_info={{_base_.dataset_info}}),
    test=dict(
        type='OneHand10KDataset',
        ann_file=f'{one_hand_data_root}/annotations/onehand10k_test.json', #onehand test set
        img_prefix=f'{test_img_root}/',
        data_cfg=data_cfg,
        pipeline=test_pipeline,
        dataset_info={{_base_.dataset_info}}),
)
