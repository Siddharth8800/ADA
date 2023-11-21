## LCS - Longest Common Subsequence
```
#include<iostream>
using namespace std;

int LCS(string a, string b) {
    int n = a.length();
    int m = b.length();
    
    int freq[n + 1][m + 1];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <=m; j++) {
            if (i == 0 || j == 0) {
                freq[i][j] = 0;
            }
            else if (a[i - 1] == b[j - 1]) {
                freq[i][j] = freq[i - 1][j - 1] + 1;
            }
            else {
                freq[i][j] = max(freq[i - 1][j], freq[i][j - 1]);
            }
        }
    }
    return freq[n][m];
}

  
int main() {
    string S1, S2;
    cout << "Enter first String: ";
    cin >> S1;
    cout << "Enter second String: ";
    cin >> S2;
    cout << "Length of LCS is " << LCS(S1, S2) << endl;
}
```

## Matrix Chain Multiplication
```
#include<iostream>
#include<climits>
using namespace std;

int main() {
   int n = 5; // size of p matrix
   int p[] = {5, 4, 6, 2, 7}; // matrix dimensions
   int m[n][n] = {0}; // to store number of multiplications
   int s[n][n] = {0}; // to store where to parenthesize
   int j, min, q;

   for (int d = 1; d < n - 1; d++) {
        for (int i = 0; i < n - d; i++) {
            j = i + d;
            min = INT_MAX;
            
            for (int k = i; k <= j - 1; k++) {
                q = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j]); 

                if (q < min) {
                    min = q;
                    s[i][j] = k;
                }
            }
            m[i][j] = min;
        }
   }
   cout << m[1][n - 1] << endl; // print last element of the matrix
}
```

## Travelling Salesman (Greedy)
```
#include<iostream>
#include<climits>
using namespace std;
  
int tsp(int n, int graph[][10], int start, int v) {
    int visited[v] = {0};
    visited[start] = 1;
    int path[v];
    int cost = 0;

    for (int count = 0; count < n - 1; count++) {
        int minCost = INT_MAX;
        int nextCity;
  
        for (int city = 0; city < n; city++) {
            if (!visited[city] && graph[start][city] < minCost) {
                minCost = graph[start][city];
                nextCity = city;
            }
        }
        visited[nextCity] = 1;
       // path[pathIndex++] = nextCity;
        cost += minCost;
        start = nextCity;
    }
    cost += graph[start][path[0]];
    // cout << "Path: ";
    // for (int i = 0; i <= n; i++) {
    //     cout << path[i] << " ";
    // }
    // cout << endl;

    return cost;
}

  

int main() {
    int n, e; // Number of cities and paths
    cout << "Enter the number of cities: ";
    cin >> n;
    cout << "Enter number of paths: ";
    cin >> e;
  
    int graph[10][10] = {0}; // Adjacency matrix to represent the graph
  
    // Input the adjacency matrix
    cout << "Enter start vertex, end vertex and weight:" << endl;
    for (int i = 0; i < e; i++) {
        int fi, si, w;
        cin >> fi >> si >> w;
        graph[fi][si] = w;
        graph[si][fi] = w;
    }

    int start; // Starting city
    cout << "Enter the starting city: ";
    cin >> start;
    int minCost = tsp(n, graph, start, n);
    cout << "Minimum cost: " << minCost << endl;
}
```

## Knapsack (Greedy)
```
#include <iostream>
#include <vector>
#include <algorithm>
#define fr(i, a, b) for(int i = a; i < b; i++)
#define all(x) (x).begin(), (x).end()
using namespace std;

class knap {  
	public:
	int id;
	float price;
	float weight;
	float ratio;
  
	void input(int i) {
		float price, weight;
		cin >> price >> weight;
		this->id = i;
		this->price = price;
		this->weight = weight;
	}

  

	void profit() {
		this->ratio = (this->price) / (this->weight);
	}

  

void print() {

cout << "ID: " << this->id << ", " << "Price: " << this->price << ", " << "Weight: " << this->weight << ", " << "Ratio: " << this->ratio << endl;
}

};

  

bool cmp(knap &a, knap &b) {
	return a.ratio > b.ratio;
}

  

int main() {
int n, k;
cout << "Enter number of Items: ";
cin >> n;
vector<knap> arr(n);
cout << "Enter Price and weight of Items: " << endl;

fr(i, 0, n) {
	arr[i].input(i);
}

  

cout << "Enter weight of Knapsack: ";
cin >> k;

fr(i, 0, n) {
	arr[i].profit();
}

  

sort(all(arr), cmp);
vector<knap> ans;
float currWeight = 0;
int i = 0;
float profit = 0;

while(currWeight < k) {
	
	if (currWeight + arr[i].weight <= k) {
	ans.push_back(arr[i]);
	currWeight += arr[i].weight;
	}

	else {

		float remainingWeight = k - currWeight;

			if(remainingWeight > 0) {			
				arr[i].price *= (remainingWeight / arr[i].weight);
				arr[i].weight = remainingWeight;
				ans.push_back(arr[i]);
				currWeight += remainingWeight;
			}

	}

	i++;

}

fr(i, 0, ans.size()) {

	ans[i].print();
	profit += arr[i].price;

}

cout << "The profit is: " << profit;

}
```

## Prims Algo
```
#include<iostream>
#include<vector>
using namespace std;
  
int findMinVertex(vector<int> &w, vector<bool> &vis, int v) {
	int minVer = -1;
	for (int i = 0; i < v; i++) {
		if (!vis[i] && (minVer == -1 || w[i] < w[minVer])) {
			minVer = i;
		}
	}
	return minVer;
}

  

void Prims(vector<vector<int> > &arr, int v) {

	vector<int> parent(v);
	vector<int> weights(v, INT_MAX);
	vector<bool> visited(v, false);
	parent[0] = -1;
	weights[0] = 0;

	for (int i = 0; i < v - 1; i++) {
		int minVer = findMinVertex(weights, visited, v);
		visited[minVer] = true;
		for (int j = 0; j < v; j++) {
			if (arr[minVer][j] && !visited[j]) {
				if (arr[minVer][j] < weights[j]) {
					weights[j] = arr[minVer][j];
					parent[j] = minVer;
				}
			}
		}
	}

	for (int i = 1; i < v; i++) {
		if (parent[i] < i) {
			cout << parent[i] << " " << i << " " << weights[i] << endl;
		}
		else {
			cout << i << " " << parent[i] << " " << weights[i] << endl;
		}
	}

}

  

int main() {

	int ver, edg;
	cout << "Enter no. of vertexs and edges: ";
	cin >> ver >> edg;
	vector<vector<int> > arr(ver, vector<int>(ver,0));
	cout << "Enter Edges with weight: " << endl;
	
	for (int i = 0; i < edg; i++) {
		int fi, si, w;
		cin >> fi >> si >> w;
		arr[fi][si] = w;
		arr[si][fi] = w;
	}
  
	Prims(arr, ver);
}
```
