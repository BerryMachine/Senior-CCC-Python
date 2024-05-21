# get initial number of streams
streams = []
for inputs in range(int(input())):
  streams.append(int(input()))

while True:
  # get the command
  event = int(input())
  
  # end the program
  if event == 77:
    break

  # split the stream
  elif event == 99:
    # get which stream is split
    stream = int(input()) - 1
    chosen_stream = streams.pop(stream)
    # get percentage of the stream to be split to the left
    split_percentage = int(input())
    left_stream = chosen_stream * split_percentage/100
    right_stream = chosen_stream - left_stream
    # add the streams to the list
    streams.insert(stream, round(left_stream))
    streams.insert(stream + 1, round(right_stream))

  # join the stream
  elif event == 88:
    # identify which streams are joined
    stream = int(input()) - 1
    left_stream = streams[stream]
    right_stream = streams[stream + 1]
    # join the streams
    streams.pop(stream)
    streams.pop(stream)
    combined_stream = left_stream + right_stream
    streams.insert(stream, combined_stream)

print(*streams)
