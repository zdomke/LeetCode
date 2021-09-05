// class Solution{		// 12ms
// 	public String intToRoman(int num){
// 		Pair<Integer, String>[] filter = new Pair[]{new Pair<>(1000, "M"),
// 			new Pair<>(900, "CM"),
// 			new Pair<>(500, "D"),
// 			new Pair<>(400, "CD"),
// 			new Pair<>(100, "C"),
// 			new Pair<>(90, "XC"),
// 			new Pair<>(50, "L"),
// 			new Pair<>(40, "XL"),
// 			new Pair<>(10, "X"),
// 			new Pair<>(9, "IX"),
// 			new Pair<>(5, "V"),
// 			new Pair<>(4, "IV"),
// 			new Pair<>(1, "I")};

// 		int ind = 0;
// 		String ret = "";
// 		while(num > 0){
// 			if(num >= filter[ind].getKey()){
// 				ret += filter[ind].getValue();
// 				num -= filter[ind].getKey();
// 			} else {
// 				ind++;
// 			}
// 		}
// 		return ret;
// 	}
// }

// class Solution{		// 8ms
// 	public String intToRoman(int num){
// 		String ret = "";
// 		while(num > 0){
// 			if(num >= 1000){
// 				ret += "M";
// 				num -= 1000;
// 			} else if(num >= 900){
// 				ret += "CM";
// 				num -= 900;
// 			} else if(num >= 500){
// 				ret += "D";
// 				num -= 500;
// 			} else if(num >= 400){
// 				ret += "CD";
// 				num -= 400;
// 			} else if(num >= 100){
// 				ret += "C";
// 				num -= 100;
// 			} else if(num >= 90){
// 				ret += "XC";
// 				num -= 90;
// 			} else if(num >= 50){
// 				ret += "L";
// 				num -= 50;
// 			} else if(num >= 40){
// 				ret += "XL";
// 				num -= 40;
// 			} else if(num >= 10){
// 				ret += "X";
// 				num -= 10;
// 			} else if(num >= 9){
// 				ret += "IX";
// 				num -= 9;
// 			} else if(num >= 5){
// 				ret += "V";
// 				num -= 5;
// 			} else if(num >= 4){
// 				ret += "IV";
// 				num -= 4;
// 			} else {
// 				ret += "I";
// 				num -= 1;
// 			}
// 		}
// 		return ret;
// 	}
// }

class Solution{		// 15ms
	public String intToRoman(int num){
        int[] vals = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] strs = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        int ind = 0;
		String ret = "";
		while(num > 0){
			if(num >= vals[ind]){
				ret += strs[ind];
				num -= vals[ind];
			} else {
                ind++;
            }
		}
		return ret;
	}
}