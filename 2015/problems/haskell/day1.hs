change x 
    | x == '(' = 1
    | x == ')' = -1
    | otherwise = 0

part1 [] = 0
part1 (x:xs) = change(x) + part1 xs

part2 input = part2helper input 1 0
    where
        part2helper _ index (-1) = index
        part2helper (x:xs) index level = part2helper xs (index+1) (level + change x)
        --part2helper [] _ _ = 1/0 -- if he can't get to basement

main = do
    input <- getLine
    print $ part1 input
    print $ part2 input