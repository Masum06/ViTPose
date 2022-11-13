'''
    for clarification: 
        The lowest number label is the base of the finger
        The highest number label is the tip of the finger
        matches proper ordrer of the data_checker process (see data_checker.py, getKeypoints())

    JSON format:
        X,Y, 2
        Wrist, IndexA-D, MiddleA-D, RingA-D, PinkyA-D, ThumbA-D
'''

dataset_info = dict(
    dataset_name='Hi510KDataset',
    paper_info=dict(),
    keypoint_info={
        0:
        dict(
            name='wrist', 
            id=0, 
            color=[255, 255, 255], 
            type='', 
            swap=''),
        1:
        dict(
            name='indexA', 
            id=1, 
            color=[255, 128, 0], 
            type='', 
            swap=''),
        2:
        dict(
            name='indexB', 
            id=2, 
            color=[255, 128, 0],
            type='',
            swap=''),
        3:
        dict(
            name='indexC',
            id=3,
            color=[255, 128, 0],
            type='',
            swap=''),
        4:
        dict(
            name='indexD',
            id=4,
            color=[255, 128, 0],
            type='', 
            swap=''),
        5:
        dict(
            name='middleA',
            id=5,
            color=[255, 153, 255], 
            type='', 
            swap=''),
        6:
        dict(
            name='middleB',
            id=6,
            color=[255, 153, 255],
            type='',
            swap=''),
        7:
        dict(
            name='middleC',
            id=7,
            color=[255, 153, 255],
            type='',
            swap=''),
        8:
        dict(
            name='middleD',
            id=8,
            color=[255, 153, 255],
            type='',
            swap=''),
        9:
        dict(
            name='ringA',
            id=9,
            color=[102, 178, 255],
            type='',
            swap=''),
        10:
        dict(
            name='ringB',
            id=10,
            color=[102, 178, 255],
            type='',
            swap=''),
        11:
        dict(
            name='ringC',
            id=11,
            color=[102, 178, 255],
            type='',
            swap=''),
        12:
        dict(
            name='ringD',
            id=12,
            color=[102, 178, 255],
            type='',
            swap=''),
        13:
        dict(
            name='pinkyA',
            id=13,
            color=[255, 51, 51],
            type='',
            swap=''),
        14:
        dict(
            name='pinkyB', 
            id=14, 
            color=[255, 51, 51], 
            type='', 
            swap=''),
        15:
        dict(
            name='pinkyC', 
            id=15, 
            color=[255, 51, 51], 
            type='', 
            swap=''),
        16:
        dict(
            name='pinkyD', 
            id=16, 
            color=[255, 51, 51], 
            type='', 
            swap=''),
        17:
        dict(
            name='thumbA', 
            id=17, 
            color=[0, 255, 0], 
            type='', 
            swap=''),
        18:
        dict(
            name='thumbB', 
            id=18, 
            color=[0, 255, 0], 
            type='', 
            swap=''),
        19:
        dict(
            name='thumbC', 
            id=19, 
            color=[0, 255, 0], 
            type='', 
            swap=''),
        20:
        dict(
            name='thumbD', 
            id=20, 
            color=[0, 255, 0], 
            type='', 
            swap='')
    },
    skeleton_info={
        0:
        dict(
            link=('wrist', 'thumbA'), 
            id=0, 
            color=[255, 128, 0]),
        1:
        dict(
            link=('thumbA', 'thumbB'), 
            id=1, 
            color=[255, 128, 0]),
        2:
        dict(
            link=('thumbB', 'thumbC'), 
            id=2, 
            color=[255, 128, 0]),
        3:
        dict(
            link=('thumbC', 'thumbD'), 
            id=3, 
            color=[255, 128, 0]),
        4:
        dict(
            link=('wrist', 'indexA'), 
            id=4, 
            color=[255, 153, 255]),
        5:
        dict(
            link=('indexA', 'indexB'), 
            id=5, 
            color=[255, 153, 255]),
        6:
        dict(
            link=('indexB', 'indexC'), 
            id=6, 
            color=[255, 153, 255]),
        7:
        dict(
            link=('indexC', 'indexD'), 
            id=7, 
            color=[255, 153, 255]),
        8:
        dict(
            link=('wrist', 'middleA'), 
            id=8, 
            color=[102, 178, 255]),
        9:
        dict(
            link=('middleA', 'middleB'),
            id=9,
            color=[102, 178, 255]),
        10:
        dict(
            link=('middleB', 'middleC'),
            id=10,
            color=[102, 178, 255]),
        11:
        dict(
            link=('middleC', 'middleD'),
            id=11,
            color=[102, 178, 255]),
        12:
        dict(
            link=('wrist', 'ringA'), 
            id=12, 
            color=[255, 51, 51]),
        13:
        dict(
            link=('ringA', 'ringB'), 
            id=13, 
            color=[255, 51, 51]),
        14:
        dict(
            link=('ringB', 'ringC'), 
            id=14, 
            color=[255, 51, 51]),
        15:
        dict(
            link=('ringC', 'ringD'), 
            id=15, 
            color=[255, 51, 51]),
        16:
        dict(
            link=('wrist', 'pinkyA'), 
            id=16, 
            color=[0, 255, 0]),
        17:
        dict(
            link=('pinkyA', 'pinkyB'), 
            id=17, 
            color=[0, 255, 0]),
        18:
        dict(
            link=('pinkyB', 'pinkyC'), 
            id=18, 
            color=[0, 255, 0]),
        19:
        dict(
            link=('pinkyC', 'pinkyD'), 
            id=19, 
            color=[0, 255, 0])
    },
    joint_weights=[1.] * 21,
    sigmas=[])