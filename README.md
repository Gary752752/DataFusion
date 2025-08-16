--cluster
----Birch 						//Balanced Iterative Reducing and Clustering using Hierarchies
----Chameleon 				//Chameleon Hierarchical clustering
----classificationTopMapXLS 		//Sort the clustering results based on a certain performance indicator
----eval 						//Clustering evaluation index(DBI,CH,DI)
----hierarchical					//agglomerative hierarchical clustering
----kmeans/newCode			// K-means-1 && K-means-2
----CalculateDistanceMatrix.java	//Euclidean distance matrix
--CreateQrel  //Create multi-dimensional points for clustering methods
--DataStruct 	//data structure
--Distance	//Implement the calculation of Euclidean distance based on multiple data structures
--evaluation
evalCombi.java		//evaluation of the Combi value
evalIndicatorJ.java		//Evaluation of the J value
evaluationMain.java	//Evaluation of the P10 NDCG MAP CAM of the result
TrecEval.java			//Calculate P10, NDCG, and MAP algorithms
--fusion_Main
fusion1_2_Main.java	//Instantiate the CombSUM algorithm and the CombMNZ algorithm
fusion3_Main.java		//Instantiate the LC algorithm
--fusionAlgorithm
//CombSUM and CombMNZ algorithms
--LCfusion //LC algorithms
--normalization //normalization method

When using this project, the following steps need to be carried out
（1）Preprocess the dataset（normalization or CreateQrel）
（2）Cluster the dataset(Birch	, Chameleon , hierarchical , kmeans or evalCombi.java or evalIndicatorJ.java or evaluationMain.java)
（3）Sort the clustering results(classificationTopMapXLS)
（4）Perform data fusion on the sorting results(fusion_Main)
（5）Evaluate the fusion results(evaluationMain.java)
