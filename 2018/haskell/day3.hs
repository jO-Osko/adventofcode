import qualified Data.Text    as Text
import qualified Data.Text.IO as Text

import qualified Data.Set as Set
import qualified Data.Map.Strict as Map

import qualified Control.Monad.State as State
import Debug.Trace
import System.CPUTime

data Range = Range 
             { uid :: Int 
             , xStart :: Int
             , yStart :: Int
             , xSize  :: Int
             , ySize  :: Int 
             } deriving (Show)

--part1 :: [Range] -> Int

part1 dat = Map.size $ Map.filter (1 <) $ part1Helper dat Map.empty
   where 
        part1Helper [] taken = taken
        part1Helper (x:xs) taken = let newMap = foldr (\loc mmp -> Map.alter ff loc mmp) taken (takenBy x) in
            part1Helper xs newMap
        ff Nothing = Just 1
        ff (Just a) = Just $ a+1 

-- Quite a bit faster
part1' dat = Map.size $ Map.filter (1 <) $ Map.unionsWith (+) (part1Helper dat)
    where 
            part1Helper [] = []
            part1Helper (x:xs) = (foldr (\loc mmp -> Map.alter ff loc mmp) Map.empty (takenBy x)) : part1Helper xs 
            ff Nothing = Just 1
            ff (Just a) = Just $ a+1 

part1'' dat = Map.size $ Map.filter (1 <) $ Map.unionsWith (+) (part1Helper dat)
    where 
        part1Helper [] = []
        part1Helper (x:xs) = Map.fromAscList (map (\a -> (a,1)) $ takenBy x) : part1Helper xs 

takenBy range = [(x,y) | x<- [left..(right-1)], y<- [top..(bottom-1)]]
    where left = xStart range
          right = left + (xSize range)
          top = yStart range
          bottom = top + (ySize range)
          toInt x = if x then 1 else 0 

--part2 :: [Range] -> Int
part2 dat = missing [1..((Set.size resultSet) + 1)] (Set.toAscList resultSet)
    where 
        part2Helper [] (taken,overlap) = overlap
        part2Helper (x:xs) (taken,overlap) = 
            let newMap = foldr folder (taken, overlap) (takenBy x) 
                folder = \loc (mmp, lap) -> (Map.insert loc xUid mmp, updater lap xUid (Map.lookup loc mmp))
                updater set cur Nothing = set
                updater set cur (Just other) = Set.insert cur (Set.insert other set)
                xUid = uid x
                in
                    part2Helper xs newMap
        resultSet = part2Helper dat (Map.empty, Set.empty)
        missing (x:xs) (y:ys) = if x == y then missing xs ys else x   

contains range (x,y) = toInt $(left <= x && x < right) && (top <= y && y < bottom)
    where left = xStart range
          right = left + (xSize range)
          top = yStart range
          bottom = top + (ySize range)
          toInt x = if x then 1 else 0 

-- Regexes seem like a good idea
parse :: [Text.Text] -> [Range]
parse dat = map parseOne dat
    where parseOne x = Range {uid=uid, xStart=fs!!0, yStart=fs!!1, xSize=sn!!0, ySize=sn!!1}
            where parseBegin t = Text.split (',' == ) (Text.init t)
                  parseEnd t = Text.split ('x' == ) t
                  firstParse = Text.split (' ' == ) x
                  uid = makeInt $ Text.tail (firstParse!!0) 
                  fs = map makeInt $ parseBegin (firstParse!!2)
                  sn = map makeInt $ parseEnd (firstParse!!3)
                
makeInt x = read (Text.unpack x) :: Int

num = 1000

--printElements :: [String] -> IO()
--printElements = mapM_ print

main = do
    ls <- fmap Text.lines (Text.readFile "../input/3.in")
    let dat = parse ls
    start <- getCPUTime
    print $ part1'' dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12
    start <- getCPUTime
    print $ part1 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12
    start <- getCPUTime
    print $ part2 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12