function count_el(arr, el) {
	var count = 1;
	for(var i=1; i<arr.length; i++) {
		if(arr[i] == el) {
			count++;
		}
	}
	return count;
}
