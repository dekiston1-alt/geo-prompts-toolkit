#!/usr/bin/env python3
"""
entity-finder.py - Finds key entities that top content in a niche mentions

Helps you understand what entities (topics, people, brands, concepts) 
dominate content in your niche.
"""

entity_database = {
    'seo': {
        'tools': ['Google Search Console', 'SEMrush', 'Ahrefs', 'Moz', 'Screaming Frog', 
                  'Google Analytics', 'Ubersuggest'],
        'concepts': ['backlinks', 'keywords', 'ranking factors', 'domain authority', 
                     'page speed', 'mobile optimization', 'schema markup', 'CTR'],
        'people': ['Neil Patel', 'Brian Dean', 'Rand Fishkin', 'John Mueller', 'Danny Sullivan'],
        'platforms': ['Google', 'Bing', 'DuckDuckGo', 'Yandex']
    },
    'pinterest': {
        'tools': ['Pinterest Analytics', 'Tailwind', 'Buffer', 'Later', 'Canva', 'Adobe Express'],
        'concepts': ['pins', 'boards', 'rich pins', 'keywords', 'seasonal content', 
                     'fresh content strategy', 'engagement rate', 'click-through rate'],
        'people': ['Erin Pfeil', 'Jenn Herman', 'Andrew Hubbard', 'Amy Landino'],
        'platforms': ['Pinterest', 'Shopify', 'Etsy', 'WordPress']
    },
    'marketing': {
        'tools': ['HubSpot', 'Mailchimp', 'Hootsuite', 'Google Ads', 'Facebook Ads Manager',
                  'Canva', 'Figma'],
        'concepts': ['customer journey', 'conversion rate', 'CTR', 'ROI', 'audience segmentation',
                     'personalization', 'A/B testing', 'attribution'],
        'people': ['Gary Vaynerchuk', 'Seth Godin', 'Ann Handley', 'David Meerman Scott'],
        'platforms': ['Facebook', 'Instagram', 'LinkedIn', 'TikTok', 'YouTube']
    },
    'wellness': {
        'tools': ['MyFitnessPal', 'Apple Health', 'Fitbit', 'Calm', 'Headspace', 'Peloton'],
        'concepts': ['gut health', 'mental health', 'sleep quality', 'immunity', 'stress management',
                     'holistic health', 'nutrition', 'self-care'],
        'people': ['Dr. Mark Hyman', 'Brené Brown', 'Deepak Chopra', 'Goop (Gwyneth Paltrow)'],
        'platforms': ['Instagram', 'TikTok', 'YouTube', 'Substack']
    },
    'gardening': {
        'tools': ['Garden Planner', 'PlantSnap', 'GardenTags', 'Smart Garden Hub', 'Almanac'],
        'concepts': ['companion planting', 'soil pH', 'composting', 'crop rotation', 
                     'pest management', 'hydration', 'organic gardening', 'pollination'],
        'people': ['Monty Don', 'P. Allen Smith', 'Carol Klein', 'Alan Titchmarsh'],
        'platforms': ['Pinterest', 'Instagram', 'YouTube', 'Reddit']
    }
}

def get_entities(niche):
    """
    Get key entities for a given niche
    """
    niche = niche.lower().strip()
    
    if niche not in entity_database:
        return None, f"Niche '{niche}' not found. Available: {', '.join(entity_database.keys())}"
    
    entities = entity_database[niche]
    return entities, None

def display_entities(niche):
    """
    Pretty print entities for a niche
    """
    entities, error = get_entities(niche)
    
    if error:
        return error
    
    output = f"\n{'='*50}\n"
    output += f"KEY ENTITIES FOR: {niche.upper()}\n"
    output += f"{'='*50}\n"
    
    output += f"\n📊 TOOLS ({len(entities['tools'])})\n"
    for tool in entities['tools']:
        output += f"  • {tool}\n"
    
    output += f"\n💡 CONCEPTS ({len(entities['concepts'])})\n"
    for concept in entities['concepts']:
        output += f"  • {concept}\n"
    
    output += f"\n👤 INFLUENCERS/EXPERTS ({len(entities['people'])})\n"
    for person in entities['people']:
        output += f"  • {person}\n"
    
    output += f"\n🌐 PLATFORMS ({len(entities['platforms'])})\n"
    for platform in entities['platforms']:
        output += f"  • {platform}\n"
    
    return output


if __name__ == "__main__":
    # Example usage
    print(display_entities('pinterest'))
    print(display_entities('seo'))
    print(display_entities('wellness'))
