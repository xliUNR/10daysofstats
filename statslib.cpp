#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

float weightedAvg(vector<long int>, vector<int>, int);
float mean(vector<long int>);
float median(vector<long int>);
float mode(vector<long int>);

// Calculates weighted average, takes in a long integer vector and a int vector of weights.
float weightedAvg(vector<long int> data, vector<int> weights, int size){
    float returnVal = 0.0f;
    float topSum = 0.0f;
    float weightSum = 0.0f;
    for(int i = 0; i < size; i++){
        topSum += data[i] * weights[i];
        weightSum += weights[i];
    }
    returnVal = (float)topSum / weightSum;
    return returnVal;
}

float mean(vector<long int>input){
    float sum=0.0f;
    int size = (int)input.size();
    for(int i = 0; i < size; i++){
        sum+=input[i];
    }
    //sum = (float)sum;
    return sum / size;
}
//input is sorted vector
float median(vector<long int>input){
    int size = (int)input.size();
    int medianIdx = size / 2;
    float returnVal = 0.0f;
    //Check for even or odd
    if( size&1 == 1){
        returnVal = input[medianIdx];
    }
    //else is even so have to take average of two median values
    else{
        returnVal = ((float)input[medianIdx] + input[medianIdx-1]) / 2;
    }

    return returnVal; 
}
//input is sorted vector
float mode(vector<long int>input){
    int size = (int)input.size();
    int primaryIdx=0;
    int workingIdx=1;
    int modeArr[size] = {0};
    int maxVal;
    int maxIdx;
    
    while(workingIdx < size){
        if( input[primaryIdx] == input[workingIdx]){
            modeArr[primaryIdx]+=1;
            workingIdx++;
        }
        else{
            primaryIdx = workingIdx;
            workingIdx++;
        }
    }
    //find max of modeArr
    maxIdx = 0;
    maxVal = modeArr[maxIdx];
    
    for( int i = 1; i < size; i++){
        if(  modeArr[i] > maxVal ){
            maxIdx = i;
            maxVal = modeArr[i];
        }
    }
    return input[maxIdx];
}
