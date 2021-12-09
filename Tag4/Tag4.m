fid = fopen("Tag4_daten.txt");
line = fgetl(fid);

input = textscan(line, '%d', 'Delimiter', ',');
input = input{1};

input_mat = textscan(fid, '%d', 'Delimiter', {' ', newline}, 'HeaderLines',1, 'MultipleDelimsAsOne', 1);
input_mat = input_mat{1};
bingo_cards = permute(reshape(input_mat, 5,5,numel(input_mat)/25), [2,1,3]);
fclose(fid)
%%
bingo_mask = zeros(size(bingo_cards));

for i = 1:length(input)
    bingo_mask = bingo_mask | (bingo_cards == input(i));
    if any(sum(bingo_mask,1)>=5, 'all')
        ind = find(sum(bingo_mask,1) >= 5);
        [row,col,page] = ind2sub(size(sum(bingo_mask,1)), ind);
        break;
    elseif any(sum(bingo_mask,2)>=5, 'all')
        ind = find(sum(bingo_mask,2) >= 5);
        [row,col,page] = ind2sub(size(sum(bingo_mask,2)), ind);
        break;
    end
end
number = input(i);
board = bingo_cards(:,:,page);
board(bingo_mask(:,:,page)) = 0;
sum_unmarked = sum(board,'all');

number*sum_unmarked

%%
bingo_mask = zeros(size(bingo_cards));
won = zeros(size(bingo_cards,3),1);
for i = 1:length(input)
    bingo_mask = bingo_mask | (bingo_cards == input(i));
    if any(sum(bingo_mask,1)>=5, 'all')
        ind = find(sum(bingo_mask,1) >= 5);
        [row,col,page] = ind2sub(size(sum(bingo_mask,1)), ind);
        won(page) = 1;
    end
    if any(sum(bingo_mask,2)>=5, 'all')
        ind = find(sum(bingo_mask,2) >= 5);
        [row,col,page] = ind2sub(size(sum(bingo_mask,2)), ind);
        won(page) = 1;
    end
    if sum(won) == length(won)-1
       ind_won = find(won==0); 
    elseif sum(won) == length(won)
        break;
    end
end
number = input(i);
board = bingo_cards(:,:,ind_won);
board(bingo_mask(:,:,ind_won)) = 0;
sum_unmarked = sum(board,'all');
number*sum_unmarked