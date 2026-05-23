#!/usr/bin/env python3
"""
pinterest-seo-keywords.py - Returns high-traffic Pinterest keywords for any niche

Keywords are categorized by traffic potential:
- High Traffic: Most searched, most competitive
- Medium Traffic: Good volume, moderate competition
- Seasonal: Spike during certain times of year
"""

keyword_database = {
    'seo': {
        'high_traffic': [
            'SEO tips',
            'SEO guide',
            'how to do SEO',
            'SEO keywords',
            'SEO for beginners',
            'best SEO tools',
            'SEO checklist',
            'SEO mistakes to avoid',
            'local SEO',
            'YouTube SEO'
        ],
        'medium_traffic': [
            'SEO audit',
            'on-page SEO',
            'technical SEO',
            'SEO copywriting',
            'SEO strategy',
            'backlink strategy',
            'keyword research',
            'search intent',
            'featured snippets',
            'core web vitals'
        ],
        'seasonal': [
            'SEO resolutions (January)',
            'spring SEO refresh (March-April)',
            'Q4 SEO strategy (September-October)'
        ]
    },
    'pinterest': {
        'high_traffic': [
            'Pinterest tips',
            'Pinterest strategy',
            'how to use Pinterest',
            'Pinterest keywords',
            'Pinterest for business',
            'Pinterest SEO',
            'Pinterest ideas',
            'viral pins',
            'pin templates',
            'Pinterest growth'
        ],
        'medium_traffic': [
            'Pinterest analytics',
            'rich pins',
            'Pinterest boards',
            'pin design ideas',
            'Pinterest content calendar',
            'Pinterest engagement',
            'Pinterest schedule',
            'Pinterest descriptions',
            'Pinterest hashtags',
            'Pinterest advertising'
        ],
        'seasonal': [
            'back to school Pinterest (July-August)',
            'holiday pin ideas (September-November)',
            'New Year Pinterest (December-January)',
            'spring home decor (March-May)'
        ]
    },
    'marketing': {
        'high_traffic': [
            'marketing tips',
            'digital marketing',
            'content marketing',
            'marketing strategy',
            'social media marketing',
            'email marketing',
            'marketing ideas',
            'marketing for small business',
            'how to market',
            'marketing examples'
        ],
        'medium_traffic': [
            'growth marketing',
            'inbound marketing',
            'marketing funnel',
            'marketing automation',
            'brand strategy',
            'customer retention',
            'conversion rate optimization',
            'marketing analytics',
            'personalization',
            'marketing psychology'
        ],
        'seasonal': [
            'Black Friday marketing (October-November)',
            'holiday marketing (September-December)',
            'New Year marketing (December-January)',
            'back to school marketing (July-August)'
        ]
    },
    'wellness': {
        'high_traffic': [
            'wellness tips',
            'healthy lifestyle',
            'mental health',
            'self care ideas',
            'wellness ideas',
            'health tips',
            'stress relief',
            'how to meditate',
            'fitness tips',
            'wellness routine'
        ],
        'medium_traffic': [
            'gut health',
            'sleep better',
            'anxiety relief',
            'holistic health',
            'natural remedies',
            'wellness products',
            'mindfulness',
            'yoga for beginners',
            'nutrition tips',
            'immune system health'
        ],
        'seasonal': [
            'New Year wellness (January)',
            'spring cleanse (March-April)',
            'summer body (May-June)',
            'fall wellness reset (September)'
        ]
    },
    'gardening': {
        'high_traffic': [
            'gardening tips',
            'garden ideas',
            'how to start a garden',
            'vegetable garden',
            'flower garden',
            'gardening for beginners',
            'raised bed garden',
            'small space gardening',
            'indoor plants',
            'herb garden'
        ],
        'medium_traffic': [
            'companion planting',
            'organic gardening',
            'container gardening',
            'garden layout',
            'pest control natural',
            'composting',
            'seed starting',
            'garden design',
            'low maintenance plants',
            'native plants'
        ],
        'seasonal': [
            'spring planting (February-April)',
            'summer garden maintenance (May-July)',
            'fall harvest (August-October)',
            'winter garden (November-January)'
        ]
    }
}

def get_keywords(niche):
    """
    Get all keywords for a niche
    """
    niche = niche.lower().strip()
    
    if niche not in keyword_database:
        return None, f"Niche '{niche}' not found. Available: {', '.join(keyword_database.keys())}"
    
    keywords = keyword_database[niche]
    return keywords, None

def display_keywords(niche):
    """
    Pretty print keywords for a niche
    """
    keywords, error = get_keywords(niche)
    
    if error:
        return error
    
    output = f"\n{'='*60}\n"
    output += f"HIGH-TRAFFIC PINTEREST KEYWORDS: {niche.upper()}\n"
    output += f"{'='*60}\n"
    
    output += f"\n🔥 HIGH TRAFFIC ({len(keywords['high_traffic'])} keywords)\n"
    output += "Most searched, highest competition, best for viral content\n"
    for i, keyword in enumerate(keywords['high_traffic'], 1):
        output += f"  {i}. {keyword}\n"
    
    output += f"\n📊 MEDIUM TRAFFIC ({len(keywords['medium_traffic'])} keywords)\n"
    output += "Good search volume, moderate competition, easier to rank\n"
    for i, keyword in enumerate(keywords['medium_traffic'], 1):
        output += f"  {i}. {keyword}\n"
    
    output += f"\n📅 SEASONAL ({len(keywords['seasonal'])} keywords)\n"
    output += "Spike at specific times of year\n"
    for i, keyword in enumerate(keywords['seasonal'], 1):
        output += f"  {i}. {keyword}\n"
    
    return output


if __name__ == "__main__":
    # Example usage
    print(display_keywords('pinterest'))
    print(display_keywords('gardening'))
    print(display_keywords('seo'))
