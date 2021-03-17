clear;
clc;
warning('off');
 

currentFolder = pwd;              
addpath(genpath(currentFolder));  

Wdd = load('dissimilarity.csv');
A = load('association_matrix.csv');
Wrr_v=load('rna_GaussianSimilarity.csv');

K1 = [];
K1(:,:,1)=Wrr_v;
K2 = [];
K2(:,:,1)=Wdd;
K1(:,:,2)=kernel_Hamads(A,1 ); %Hamming distance
K2(:,:,2)=kernel_Hamads(A,2 );
K_COM1=SKF({K1(:,:,1),K1(:,:,2)},36,10,0.1);
K_COM2=SKF({K2(:,:,1),K2(:,:,2)},36,10,0.1);
interMartix=WKNKN( A, K_COM1, K_COM2, 5, 1 );
