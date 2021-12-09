fid = fopen("Tag5_daten.txt");
input = textscan(fid, '%d', 'Delimiter', ',');
input = cell2mat(input);

fclose(fid);
%%
len = 80;

for i = 1:len
    input = input - 1;
    num_new = numel(find(input == -1));
    input = cat(1, input, repmat(8,num_new,1));
    input(input==-1) = 6;
end

numel(input)
%%
fid = fopen("Tag5_daten.txt");
input = textscan(fid, '%d', 'Delimiter', ',');
input = cell2mat(input);

fclose(fid);
%% 
len = 80;
gr = 0:8;
gc = zeros(size(gr));
for i = 1:length(input)
    for j = 1:length(gr)
        if input(i) == gr(j)
            gc(j) = gc(j)+1;
        end
    end
end

k = gc;
for i = 1:len
    k = circshift(k, -1);
    k(7) = k(7)+k(end);
end

sum(k)