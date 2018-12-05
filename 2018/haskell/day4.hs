{-# LANGUAGE NamedFieldPuns, RecordWildCards #-}
import qualified Data.Text    as Text
import qualified Data.Text.IO as Text

import qualified Data.List    as List

import qualified Data.Set as Set
import qualified Data.Map.Strict as Map
import qualified Data.IntMap.Strict as IntMap

import qualified Data.DateTime as Time

import qualified Control.Monad.State as State
import Debug.Trace
import System.CPUTime

--part1 :: [(Action, Time.DateTime)] -> Int
part1 (((BeginsShift uid), time):xs) = cInd * mMax
    where
        timings = part' xs uid (WokeUp, time) IntMap.empty
        res = IntMap.toList timings
        (cInd, cMax, mMax) = guardsMax res (0,0,0)
        
        


-- Sleepy, cant even think of a nice abstraction
myMax [] cSum (cInd, cMax) = (cInd, cSum, cMax)
myMax ((k,val):xs) cSum (cInd,cMax) = myMax xs (cSum + val) $ if val > cMax then (k, val) else (cInd, cMax) 

guardsMax [] (cInd, cMax, mMax) = (cInd, cMax, mMax)
guardsMax ((gInd,vals):xs) (cInd, cMax, mMax) = guardsMax xs $ if tSum > cMax then (gInd, tSum, mInd) else (cInd, cMax, mMax)
    where
      (mInd, tSum, cmMax) = myMax (IntMap.toList vals) 0 (0,0)

guardsMax2 [] (cInd, cMax, mMax) = (cInd, cMax, mMax)
guardsMax2 ((gInd,vals):xs) (cInd, cMax, mMax) = guardsMax2 xs $ if cmMax > cMax then (gInd, cmMax, mInd) else (cInd, cMax, mMax)
    where
    (mInd, tSum, cmMax) = myMax (IntMap.toList vals) 0 (0,0)

data ActionType = WokeUp
                | FellAsleep

part' :: [(Action, Time.DateTime)] -> 
            Int -> (ActionType, Time.DateTime) -> IntMap.IntMap (IntMap.IntMap Int)  -> IntMap.IntMap (IntMap.IntMap Int) 
part' [] _ _ takenMinutes = takenMinutes 
part' (((BeginsShift uid), time):xs) _ _ takenMinutes = part' xs uid (WokeUp, time) takenMinutes
part' ((FallsAsleep, time):xs) uid _ takenMinutes = part' xs uid (FellAsleep, time) takenMinutes
part' ((WakesUp, endTime):xs) uid (FellAsleep, startTime) takenMinutes = 
    part' xs uid (WokeUp, endTime) newTakenMinutes
    where 
        newTimes newTime = if not (newTime < endTime) then [] else (getMinutes newTime,1) : newTimes (fixSeconds (Time.addSeconds 60 newTime))
        updatedMap = IntMap.fromListWith (+) (newTimes startTime)  
        newTakenMinutes = IntMap.alter (\x -> Just (IntMap.unionWith (+) (getDefault x) updatedMap))uid takenMinutes


getDefault Nothing = IntMap.empty
getDefault (Just s) = s
--part2 :: [Range] -> Int
part2 (((BeginsShift uid), time):xs) = cInd * mMax
    where
        timings = part' xs uid (WokeUp, time) IntMap.empty
        res = IntMap.toList timings
        (cInd, cMax, mMax) = guardsMax2 res (0,0,0)

data Action = WakesUp
            | FallsAsleep
            | BeginsShift Int 
            deriving (Show)

getMinutes x = let (_,_,_,_,y,_) = Time.toGregorian x in y

fixSeconds x = let (y,month,day,hou,min,sec) = Time.toGregorian x in Time.fromGregorian y month day hou (min + if sec==0 then 0 else 1)  0

parse dat = map parseOne $ List.sort dat
    where parseOne x = (action, Time.fromGregorian (2018) month day hour minutes 0)
            where firstParse = Text.split (' ' == ) (Text.tail x)
                  (year:month:day:_) = map makeInt (Text.split ('-' ==) (firstParse!!0))
                  (hour:minutes:_) = map makeInt (Text.split (':' == ) (Text.init (firstParse!!1)))
                  act = Text.unpack (firstParse!!2)
                  action = case act of 
                    "falls" -> FallsAsleep
                    "wakes" -> WakesUp 
                    "Guard" -> BeginsShift (makeInt $ Text.tail (firstParse!!3))

makeInt x = read (Text.unpack x) :: Int

num = 1000

--printElements :: [String] -> IO()
--printElements = mapM_ print

main = do
    ls <- fmap Text.lines (Text.readFile "../input/4.in")
    let dat = parse ls
    start <- getCPUTime
    print $ part1 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12    
    start <- getCPUTime
    print $ part2 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12