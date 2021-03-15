function count_el(arr, el) {
	var count = 0;
	for(var j=0; j<arr.length; j++) {
		if(arr[j] == el) {
			count++;
		}
	}
	return count;
}
