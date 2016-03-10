media_item = reaper.GetMediaItem(0, 10)
take = reaper.GetTake(media_item, 0)

starts = {}

file = io.open("D:/ML/beats/Cockroach_King.txt", "w")
io.output(file)

for i = 0, reaper.MIDI_CountEvts(take) - 1, 1 do 
  retval, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut
   = reaper.MIDI_GetNote(take, i)
  
  seconds = reaper.MIDI_GetProjTimeFromPPQPos(take, startppqposOut)
  milliseconds = math.ceil(seconds * 1000)
  
  starts[i] = milliseconds
  
  reaper.ShowConsoleMsg(string.format("%s\n", milliseconds))
  io.write(string.format("%s\n", milliseconds))
end

io.close(file)
