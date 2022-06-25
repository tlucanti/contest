for t in range(int(input())):
	W, H = map(int, input().split())
	x1, y1, x2, y2 = map(int, input().split())
	w, h = map(int, input().split())
	if x2 - x1 + w > W and y2 - y1 + h > H:
		print(-1)
		continue
	max_x = max(x1, W - x2)
	max_y = max(y1, H - y2)
	x = min(abs(w - x1), abs(x2 - (W - w)))
	y = min(abs(h - y1), abs(y2 - (H - h)))
	if max_x >= w or max_y >= h:
		print(0)
		continue
	if x2 - x1 + w <= W and y2 - y1 + h <= H:
		print(min(x, y))
	elif x2 - x1 + w <= W:
		print(x)
	else:
		print(y)
