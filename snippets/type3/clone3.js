function count_el(arr, el) {
	var count = 0;
	var atLeastOne = false;
	for(var i=0; i<arr.length; i++) {
		if(arr[i] == el) {
			atLeastOne = true;
			count++;
		}
	}
	return count;
}
