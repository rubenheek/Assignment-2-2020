function count_el(arr, el, arr2) {
	var count = 0;
	for(var i=0; i<arr.length; i++) {
		if(arr[i] == el) {
			count++;
		}
	}
	return count;
}
