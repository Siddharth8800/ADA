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

## Kruskals Algo
```
#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

class edge {

	public:
	int src;
	int dst;
	int w;
	
	void input() {
		int s, d, w;
		cout << "Enter source dstination and weight: ";
		cin >> s >> d >> w;
		this->src = s;
		this->dst = d;
		this->w = w;
		
	}

	void print() {
		cout << "Start: " << this->src << endl;
		cout << "End: " << this->dst << endl;
		cout << "Weight: " << this->w << endl;
	}
	
};

  

bool cmp(edge &a, edge &b) {
	return a.w < b.w;
}

  

int checkParent(int src, int *ufind) {
	if (ufind[src] == src) {
		return src;
	}
	
	return checkParent(ufind[src], ufind);
}

  

int main() {

	int ver, edg;
	cout << "Enter no. of vertexs and edges: ";
	cin >> ver >> edg;
	vector<edge> out(edg - 1);
	vector<edge> arr(edg);
	
	int *ufind = new int[ver];
	
	for (int i = 0; i < ver; i++) {
		ufind[i] = i; 
	}
	
	for (int i = 0; i < edg; i++) {
		arr[i].input();
	}
	
	sort(arr.begin(), arr.end(), cmp);
	int count = 0;
	int i = 0;
	
	while(count != ver - 1) {
		edge current = arr[i];
		int srcP = checkParent(current.src, ufind);	
		int dstP = checkParent(current.dst, ufind);

		if (srcP != dstP) {
			out[count] = current;
			count++;
			ufind[srcP] = dstP;
		}
	i++;
	}
	
	for (int i = 0; i < out.size(); i++) {
	
		out[i].print();
		cout << endl;
	
	}

}
```

## DFS
```
void printDFS(vector<vector<int> > &arr, int sv, vector<bool> &visited) {
    cout << sv << " ";
    visited[sv] = true;
    for (int i = 0; i < arr.size(); i++) {
        if (i == sv) {
            continue;
        }

        if (arr[sv][i] == 1 && visited[i] == false) {
            printDFS(arr, i, visited);
        }
    }

}

int main() {

    int ver, edg;
    cout << "Enter the number of vertices: ";
    cin >> ver;
    cout << "Enter the number of edges: ";
    cin >> edg;
    vector<vector<int> > graph(ver);
    
    for(int i = 0; i < ver; i++) {
        graph[i] = vector<int>(ver,0);
    }

  

    cout << "Enter the edges and weight: " << endl;
    for (int i = 0; i < edg; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    printDFS(graph, 0, visited);  
}
```

## BFS
```
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
  
void printBFS(vector<vector<int> > arr, int sv, vector<bool> &visited) {
    queue<int> process;
    process.push(sv);
    visited[sv] = true;
    
    while (!process.empty()) {
        int top = process.front();
        cout << top << " ";
        process.pop();
        for(int i = 0; i < arr.size(); i++) {
            if (arr[top][i] == 1 && visited[i] == false) {
                process.push(i);
                visited[i] = true;
            }
        }
    }
}

  
  

int main() {
    int ver, edg;
    cout << "Enter no. of vertexs and edges: ";
    cin >> ver >> edg;
    vector<vector<int> > arr(ver, vector<int>(ver,0));
    cout << "Enter Edges: " << endl;
    
    for (int i = 0; i < edg; i++) {
        int fi, si;
        cin >> fi >> si;
        arr[fi][si] = 1;
        arr[si][fi] = 1;
    }
    vector<bool> visited(ver, false);
    printBFS(arr, 0, visited);

}
```

## Two Sum
```
#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

  
vector<pair<int,int>> twoSum(vector<int>& arr, int target, int n)
{
    sort(arr.begin(), arr.end());
    int j = n - 1, i = 0;
    int sum = 0;
    vector<pair<int,int>> ans;    
    while(i < j) {
        sum = arr[i] + arr[j];
        if (sum > target) {
            j--;
        }
        else if (sum < target) {
            i++;
        }
        else {
            ans.push_back(make_pair(arr[i], arr[j]));
            i++;
            j--;
        }
    }

    if (!ans.size()) {
        ans.push_back(make_pair(-1, -1));
    }
    return ans;
}

  
  
int main() {
    int n, target;
    cout << "Enter number of elements: ";
    cin >> n;
    vector<int> arr(n);

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter Target Sum: ";
    cin >> target;
    vector<pair<int, int>> ans = twoSum(arr, target, n);
    cout << "The answer is.." << endl;
    for (auto i: ans) {
        cout << i.first << " " << i.second << endl;
    }
}
```

## Three Sum
```
#include <iostream>
using namespace std;

bool find3Numbers(int A[], int arr_size, int sum)
{
    for (int i = 0; i < arr_size - 2; i++) {

        for (int j = i + 1; j < arr_size - 1; j++)
        {
            for (int k = j + 1; k < arr_size; k++)
            {
                if (A[i] + A[j] + A[k] == sum)
                {
                    cout << "Triplet is " << A[i] <<
                        ", " << A[j] << ", " << A[k] << endl;
                    return true;
                }
            }
        }
    }
    return false;
}

  
int main()
{
    int n;
    int A[100];
    cout << "Enter size of Array: ";
    cin >> n;
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    int sum;
    cout << "Enter Sum: ";
    cin >> sum;
    find3Numbers(A, n, sum);
}
```

## Merge Sort
```
#include<iostream>
using namespace std;

  
void merge(int arr[], int start, int mid, int end) {
    int n1 = mid - start + 1;
    int n2 = end - mid;
    int left[n1], right[n2];
  
    for (int i = 0; i < n1; i++)
        left[i] = arr[start + i];
    for (int j = 0; j < n2; j++)
        right[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = start;

    while (i < n1 && j < n2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

  

void mergeSort(int arr[], int start, int end) {
    if (start >= end)
        return;

    int mid = start + (end - start) / 2;
    mergeSort(arr, start, mid);
    mergeSort(arr, mid + 1, end);
    merge(arr, start, mid, end);
}

  

int main() {

    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements: ";
    
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    mergeSort(arr, 0, n - 1);
    cout << "Sorted array: ";

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
```

## Quick Sort
```
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

  
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

  

void printArray(const vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

  

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    quickSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    printArray(arr);
}
```

## Binary Search
```
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int iterativeBinarySearch(vector<int>& nums, int target, int n) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    vector<int> nums(n);
    cout << "Enter the elements of the array in sorted order: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int target;
    cout << "Enter the target value: ";
    cin >> target;
    int result = iterativeBinarySearch(nums, target, nums.size());
    if (result != -1) {
        cout << "Element found at index " << result << endl;
    } else {
        cout << "Element not found" << endl;
    }
}
```

## All Paths to a destination
```
#include<iostream>
#include<vector>
#define fr(i, a, b) for(int i = a; i < b; i++)
using namespace std;

void allPathsHelp(vector<vector<bool> > &arr, vector<bool> &visited, int s, vector<int> &smallAns) {
    visited[s] = true;
    smallAns.push_back(s);
    fr(i, 0, arr.size()) {
        if (i == s) {
            continue;
        }
        if(arr[s][i] && !visited[i]) {
            allPathsHelp(arr, visited, i, smallAns);
        }
    }
}


vector<vector<int> > allPaths(vector<vector<bool> > arr) {
    vector<bool> visited(arr.size(), false);
    vector<vector<int> > ans;
    fr(i, 0, arr.size()) {
        if(!visited[i]) {
            vector<int> smallAns;
            allPathsHelp(arr, visited, i, smallAns);
            ans.push_back(smallAns);
        }
    }
    return ans;
}
  
int main() {
    int ver, edg;
    cout << "Enter no. of vertexs and edges: ";
    cin >> ver >> edg;
    vector<vector<bool> > arr(ver, vector<bool>(ver,false));
    cout << "Enter Edges: " << endl;
    for (int i = 0; i < edg; i++) {
        int fi, si;
        cin >> fi >> si;
        arr[fi][si] = true;
        arr[si][fi] = true;
    }

    vector<vector<int> > ans = allPaths(arr);
    fr(i, 0, ans.size()) {
        fr(j, 0, ans[i].size()) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}
```

## Knapsack (DP)
```
#include<iostream>
using namespace std;
  
int knapsack(int weights[], int values[], int n, int W) {

    int dp[n + 1][W + 1];

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (weights[i - 1] <= w)
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][W];
}

int main() {
    int n;
    cout << "Enter the number of items: ";
    cin >> n;
    int weights[n];
    int values[n];
    cout << "Enter the weights of the items: ";

    for (int i = 0; i < n; i++) {
        cin >> weights[i];

    }

    cout << "Enter the values of the items: ";
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }


    int W;
    cout << "Enter the maximum weight capacity: ";
    cin >> W;
    int maxValue = knapsack(weights, values, n, W);
    cout << "Maximum value: " << maxValue << endl;
}
```
