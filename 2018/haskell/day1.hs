import qualified Data.Text    as Text
import qualified Data.Text.IO as Text

import qualified Data.Set as Set

import qualified Control.Monad.State as State

import System.CPUTime

part1 :: [Int] -> Int
part1 = sum

part3 input = State.evalState (part2helper $ cycle input) (Set.singleton 0, 0)

part2 input =
    play (cycle input) (Set.singleton 0) 0
    where play (x:xs) set cur = let next = cur + x in if Set.member next set
            then next
            else play xs (Set.insert next set) next

part2helper :: [Int] -> State.State ((Set.Set Int), Int) Int
part2helper (x:xs) = do
    (takenNums, last) <- State.get
    let current = last + x
    if Set.member current takenNums then
        do return current
    else
        do 
            State.put (Set.insert current takenNums, current)
            part2helper xs

main = do
    ls <- fmap Text.lines (Text.readFile "../input/1.in")
    let dat = map (\x -> read (filter ('+' /=) $ Text.unpack x) :: Int) ls
    print $ part1 dat
    start <- getCPUTime
    print $ part2 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12
    start <- getCPUTime
    print $ part3 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12
