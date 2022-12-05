Github Link: https://github.com/liuhanmo321/GCL_with_Aug

## Get Started
 
 To run the code, the following packages are required to be installed:
 
* python==3.7.10
* scipy==1.5.2
* numpy==1.19.1
* torch==1.7.1
* networkx==2.5
* scikit-learn~=0.23.2
* matplotlib==3.4.1
* ogb==1.3.1
* dgl==0.6.1
* dgllife==0.2.6

## Directly run experiments

To get the results for baselines directly, use the following command. Use --aug=True for augmented baselines, use --aug=False for not augmented baselines.

The results are stored in \results folder, the ones end with "Aug:1" are augmented results, while the ones with "Aug:1" are not augmented results.

```
python run.py --dataset=citeseer --gpu=1 --aug=True
```

 ## Dataset Usages
 
 ### Importing the Datasets
 For importing citeseer dataset, use the following command in python:
 
 ``` python
 from backbones.utils import NodeLevelDataset
 dataset = NodeLevelDataset('citeseer')
```
 
 ## Pipeline Usages
 
  Below is the example to run the 'LwF' baseline with GCN backbone. To apply augmentation, please mention aug as True, else turn it to False.

  If errors reported in windows system, please call --replace_illegal_char=True.
 
 ```
 python train.py --dataset citeseer \
        --method lwf \
        --backbone GCN \
        --gpu 0 \
        --aug True
 ```

For the baselines with tunable hyper-parameters, the search space of parameters are shown in the args in train.py file.

 ## Final AP and Final AF

 Final AP (or AC in the report) and AF refers to the AP and AF after learning the entire task sequence and is the most compact way to show the performance of a model. Suppose an experiment result is stored via the path ```result_path```, the final AP and AF could be obtained by the following code.
 ``` python
 from visualize import shown_final_APAF
 shown_final_APAF("result_path")
 ```
 The outputs with standard deviation are in LaTex form for making it easy to be copied and pasted into a LaTex table.

By default, the results are stored in results folder. For testing resutls, please find the files with 'te' at the beginning, which are used for final performance evaluation.


The implementation is adopted from a benchmark paper, which was published in the datasets and benchmarks track of NeurIPS 2022 [(paper link)](https://openreview.net/forum?id=5wNiiIDynDF).