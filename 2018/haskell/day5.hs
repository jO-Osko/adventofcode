{-# LANGUAGE NamedFieldPuns, RecordWildCards #-}
import qualified Data.Text    as Text
import qualified Data.Text.IO as Text

import qualified Data.List    as List

import qualified Data.Set as Set
import qualified Data.Map.Strict as Map
import qualified Data.IntMap.Strict as IntMap

import qualified Data.DateTime as Time

import qualified Data.Char as Char

import Data.Sequence

import qualified Control.Monad.State as State
import Debug.Trace
import System.CPUTime

part1 dat = Data.Sequence.length $ process Empty f s xxs
    where
        start = fromList dat
        (f, s, xxs) = unpackRight start

unpackRight right = (f, s, xxs)
    where
        (f :< xs) = viewl right
        (s :< xxs) = viewl xs

process:: Seq Char -> Char -> Char -> Seq Char -> Seq Char
process Empty x y (f :<| s :<| xxs) = 
    case cond x y of 
        True -> process Empty f s xxs
        False -> process (Empty :|> x) y f (s :<| xxs)
process res x y Empty = 
    case cond x y of 
        True -> res
        False -> res :|> x :|> y
process (left :|> prev) x y (next :<| right) = 
    case cond x y of 
        True -> process left prev next right
        False -> process (left :|> prev :|> x) y next right 

cond x y = (Char.toLower x == Char.toLower y) && (isDifferent x y)

isDifferent x y = (Char.isLower x && Char.isUpper y) || (Char.isLower y && Char.isUpper x)

part2 dat = minimum $ map part1 ([ List.filter (\x -> j /= Char.toLower x ) dat | j <- ['a'..'z']  ])

parse dat = Text.unpack $ head dat

main = do
    ls <- fmap Text.lines (Text.readFile "../input/5.in")
    let dat = parse ls
    start <- getCPUTime
    print $ part1 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12    
    start <- getCPUTime
    print $ part2 dat
    end <- getCPUTime
    print $ fromIntegral (end - start) / 10^12