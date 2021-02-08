import time


def selection_sort(arr, displayBar, animSpeed):
	for i in range(len(arr)):
		selected_index = i
		for j in range(i+1,len(arr)):
			if arr[selected_index] > arr[j]:
				selected_index = j
				displayBar(arr, ['blue' if a == i or a ==j else 'red' for a in range(len(arr))])
				time.sleep(animSpeed)
		arr[i], arr[selected_index] = arr[selected_index], arr[i]
	displayBar(arr, ['blue' for a in range(len(arr))])

