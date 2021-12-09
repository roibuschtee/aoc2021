fid = fopen("Tag2_daten.txt");
C = textscan(fid, '%s %d');
input = textscan(fid, '%s %d', 'Delimiter', {' ','\n'});
%%
pos = [0, 0];
for i = 1:size(C{1},1)
    if contains(C{1}{i}, "forward")
        
    elseif contains(C{1}{i}, "up")
        
    elseif contains(C{1}{i}, "down")
        
    end
end