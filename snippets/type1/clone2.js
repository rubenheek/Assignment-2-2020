function count_el(arr, el) {
	var count = 0; // initialise counter
	/*
	iterate over the array,
  check if the array element is equal to el
	if so, increase the counter
	*/
	for(var i=0; i<arr.length; i++) {
		if(arr[i] == el) {
			count++;
		}
	}
	// return final result
	return count;
}
