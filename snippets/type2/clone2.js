function count_el(arr, el) {
	var c = 0;
	for(var i=0; i<arr.length; i++) {
		if(arr[i] == el) {
			c++;
		}
	}
	return c;
}
