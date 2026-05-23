#!/usr/bin/env python3
"""
geo-checker.py - Scores content 0-100 for AI citation readiness

Scores content based on:
- Statistics (verifiable numbers)
- Authoritative language (expert voice)
- Definitions (explaining concepts clearly)
- Q&A format (answering common questions)
- Word count (comprehensive coverage)
- Citations (sources and references)
"""

import re
from collections import Counter

def score_citation_readiness(content):
    """
    Score content for AI citation readiness (0-100)
    """
    score = 0
    feedback = []
    
    # Check for statistics/numbers (0-15 points)
    stats_pattern = r'\b\d+[%]?\b|\d+\s*(million|billion|thousand|%|dollars?|people)'
    stats = len(re.findall(stats_pattern, content, re.IGNORECASE))
    stats_score = min(15, stats * 2)
    score += stats_score
    feedback.append(f"Statistics: {stats_score}/15 ({stats} found)")
    
    # Check for authoritative language (0-15 points)
    authority_keywords = ['research shows', 'studies indicate', 'experts agree', 'proven', 
                          'established', 'scientific', 'according to', 'data shows']
    authority_matches = sum(1 for keyword in authority_keywords if keyword.lower() in content.lower())
    authority_score = min(15, authority_matches * 3)
    score += authority_score
    feedback.append(f"Authority: {authority_score}/15 ({authority_matches} phrases)")
    
    # Check for definitions/explanations (0-15 points)
    definition_patterns = [r'is defined as', r'means that', r'refers to', r'is the', r'definition:']
    def_matches = sum(len(re.findall(pattern, content, re.IGNORECASE)) for pattern in definition_patterns)
    def_score = min(15, def_matches * 2)
    score += def_score
    feedback.append(f"Definitions: {def_score}/15 ({def_matches} found)")
    
    # Check for Q&A format (0-15 points)
    qa_pattern = r'\?\s*\n|\?\s{2,}|Q:|Why|How|What'
    qa_matches = len(re.findall(qa_pattern, content))
    qa_score = min(15, qa_matches)
    score += qa_score
    feedback.append(f"Q&A Format: {qa_score}/15 ({qa_matches} questions)")
    
    # Check word count (0-15 points)
    word_count = len(content.split())
    if word_count >= 2000:
        wordcount_score = 15
    elif word_count >= 1000:
        wordcount_score = 10
    elif word_count >= 500:
        wordcount_score = 7
    elif word_count >= 200:
        wordcount_score = 3
    else:
        wordcount_score = 0
    score += wordcount_score
    feedback.append(f"Word Count: {wordcount_score}/15 ({word_count} words)")
    
    # Check for citations/sources (0-10 points)
    citation_patterns = [r'\(https?://[^)]+\)', r'\[\d+\]', r'Source:', r'Reference:',
                        r'According to [A-Z]', r'From [A-Z]']
    citation_matches = sum(len(re.findall(pattern, content)) for pattern in citation_patterns)
    citation_score = min(10, citation_matches * 2)
    score += citation_score
    feedback.append(f"Citations: {citation_score}/10 ({citation_matches} found)")
    
    return min(100, score), feedback, word_count


if __name__ == "__main__":
    # Example usage
    sample_content = """
    SEO Statistics and Research
    
    What is SEO? SEO is defined as the practice of optimizing your website to rank higher 
    in search engines. According to recent studies, over 68% of online experiences begin with 
    a search engine.
    
    Key Facts:
    - Over 5.6 billion searches per day on Google
    - 72% of internet users research products online
    - Websites on the first page get 91% of traffic
    
    How does SEO work? SEO works by improving both technical and content aspects. Research shows 
    that pages with quality backlinks rank 34% higher. The average top-ranking page has 1,447 words.
    
    Why is SEO important? Studies indicate that organic search drives 40-80% more traffic than 
    paid search. Establishing authority through SEO builds trust.
    
    (Reference: https://example.com/seo-research)
    (Source: https://example.com/statistics)
    """
    
    score, feedback, word_count = score_citation_readiness(sample_content)
    
    print("\n" + "="*50)
    print(f"CITATION READINESS SCORE: {score}/100")
    print("="*50)
    for item in feedback:
        print(f"  • {item}")
    print(f"\nTotal words: {word_count}")
    print("\nResult: Content is", end=" ")
    if score >= 80:
        print("EXCELLENT for AI citations ✓")
    elif score >= 60:
        print("GOOD for AI citations ✓")
    elif score >= 40:
        print("MODERATE - needs improvement")
    else:
        print("POOR - significant improvements needed")
