# FuzzySearchPY

## What is this?

A "hand written" (obviously not hand written because it's typed) port of [fuzzy-search](https://www.npmjs.com/package/fuzzy-search)

## Why was this made?

I like that package and I want to use it in python

## How to use this?

You create a FuzzySearcher instance
```
fuzzy_searcher = FuzzySearcher(hay_stack, keys, options)
```
Options is a dictionary that contains "caseSensitive" and "sort",
They need to be booleans, both default to false.
Keys are needed if you want to search for dictionaries.
Hay_stack can be a list of strings of a list of dictionaries