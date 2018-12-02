import qualified Data.Text    as Text
import qualified Data.Text.IO as Text

import qualified Data.Set as Set
import qualified Data.Map.Strict as Map

import qualified Control.Monad.State as State

import System.CPUTime

--part1 :: [String] -> Int
part1 dat = twos*threes
    where mmap = map countRepeats dat
          folder (chr, val) (two, three) 
                | val == 2 = (True, three)
                | val == 3 = (two, True)
                | otherwise = (two, three)
          counts = map (\x -> foldr folder (False, False) (Map.toList x)) mmap
         
          (twos, threes) = (counter (map fst counts) 0, counter (map snd counts) 0)
          counter [] n= n
          counter (x:xs) n = counter xs (n + if x then 1 else 0) 

countRepeats word = Map.fromListWith (+) (map (\x -> (x, 1)) word)

part2 :: [String] -> String
part2 dat = head $ findFst dat
  where
    findFst (x:xs) = findSnd xs x ++ findFst xs
    findSnd (y:ys) x = if dst x y == 1 then [map fst $ filter (\(a,b) -> a==b ) (zip x y) ] else findSnd ys x
    findSnd [] _ = []
    dst x y = sum $ map (\(a,b) -> if a == b then 0 else 1) (zip x y)

main = do
    ls <- fmap Text.lines (Text.readFile "../input/2.in")
    let dat = map Text.unpack ls
    print $ part1 dat
    print $ part2 dat