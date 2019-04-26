int maxSubarray(int[] matrix) {

     int res=0, max=Integer.MIN_VALUE;    
    for (int i=0; i<matrix.length; i++)        
    {
        int cur=0;
        for (int j=i; j<matrix.length; j++)        
        {    
            cur+=matrix[j];
            res=Math.max(cur, res);
        }    
    }    
    return res;

}