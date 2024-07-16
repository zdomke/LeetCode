import java.util.*;

class Solution{
    public boolean checkIfExist(int[] arr){
        Set<Integer> set = new HashSet<>();

        for(int i : arr){
            if(set.contains(i)) return true;
            set.add(i * 2);
            if(i % 2 == 0)
                set.add(i / 2);
        }
        return false;
    }
}