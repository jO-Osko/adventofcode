import Data.List.Split (splitOn)
import Data.List (sort)
import Prelude hiding (readList)
import Control.Applicative
import Control.Monad
import Control.Monad.Trans
import Control.Monad.Trans.Maybe
import Data.Maybe

part1 input = sum (map (\x -> part1helper $sort x) input)
    where
        part1helper [a,b,c] = 2*(a*b + a*c + b*c) + a*b

part2 input = sum (map (\x -> part2helper $sort x) input)
    where
        part2helper [a,b,c] = 2*(a+b) + a*b*c


readList :: IO [String]
readList = fmap (fromMaybe []) $ runMaybeT $ many $ do
  l <- lift getLine
  guard $ not $ null l
  return l


make_int dat = map (\x -> read x ::Int) (splitOn "x" dat)
  
main = do
    input <- readList
    let split_data = map make_int input
    print split_data
    print $ part1 split_data
    print $ part2 split_data