function count_el(arr, el) {
	var count = 0;

	for(var i=0; i<arr.length; i++) {
		if(arr[i] == el) {
			count++;
		}
	}

	return count;
}
