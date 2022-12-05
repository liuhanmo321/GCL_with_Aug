import os

import argparse

parser = argparse.ArgumentParser(description='CGLB')
parser.add_argument("--dataset", type=str, default='Products-CL', help='Products-CL, Reddit-CL, Arxiv-CL, CoraFull-CL')
parser.add_argument("--gpu", type=int, default=0, help="which GPU to use.")
parser.add_argument("--aug", type=str, default='False', help="augmentation")
parser.add_argument("--repeats", type=int, default=5, help="augmentation")

args = parser.parse_args()

print(args.aug)
os.system(f"python train.py --method=bare --dataset={args.dataset} --epochs=200 --aug={args.aug} --repeats=5 --gpu={args.gpu}")
os.system(f"python train.py --method=ewc --dataset={args.dataset} --epochs=200 --aug={args.aug} --repeats=5 --gpu={args.gpu} ")
os.system(f"python train.py --method=lwf --dataset={args.dataset} --epochs=200 --aug={args.aug} --repeats=5 --gpu={args.gpu} ")
os.system(f"python train.py --method=twp --dataset={args.dataset} --epochs=200 --aug={args.aug} --repeats=5 --gpu={args.gpu} ")
os.system(f"python train.py --method=ergnn --dataset={args.dataset} --epochs=200 --aug={args.aug} --repeats=5 --gpu={args.gpu}")

if args.aug == "False":
    os.system(f"python train.py --method=lwf --dataset={args.dataset} --epochs=200 --aug=False --repeats=5 --gpu={args.gpu} ")