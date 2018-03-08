int crossingSum(int[][] matrix, int a, int b) {

    int res=0, max=Integer.MIN_VALUE;    
   for (int i=0; i<matrix.length; i++)        
   {
       res+=matrix[i][b];
   }    
   
       for (int j=0; j<matrix[0].length; j++)        
       {    
           if(j==b) continue;
       res+=matrix[a][j];
       }    
       
   return res;
   

}