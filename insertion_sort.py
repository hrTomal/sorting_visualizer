import time

def insertion_sort(arr, displayBar, animSpeed):
	for i in range(len(arr)):
		selected = arr[i]
		j = i-1
		while j>=0 and selected < arr[j]:
			arr[j+1] = arr[j]
			displayBar(arr, ['blue' if a == j or a ==j+1 else 'red' for a in range(len(arr))])
			j -= 1
		arr[j+1] = selected
		time.sleep(animSpeed)
	displayBar(arr, ['blue' for a in range(len(arr))])
