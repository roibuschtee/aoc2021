using DelimitedFiles

input = readdlm("Tag6/Tag5_daten_test.txt", ',', Int64, '\n');

fishes = zeros(Int64, 9)
a = zeros(Int64, 9)
for element in input
    fishes[element+1] += 1
end

steps = 80
for i in 1:80
    b = circshift(fishes, -1)
    
    fishes[7] += fishes[end]
end
a=1
print(sum(fishes))