#!/usr/bin/env python3
"""
Example Passport Generator for Cultural World Adaptive Nexus

This script demonstrates how to:
1. Generate a demo cultural passport JSON
2. Optionally call the FastAPI endpoint to create it (if API is running)
3. Save the passport to a local file

Usage:
    python example_passport.py [--api-url http://localhost:8000] [--output passport.json]

Author: Comandante Hebron Nexus
License: MIT + Nexus Ethical Clauses
"""

import json
import random
import argparse
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import sys

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️  'requests' library not available. Will only save to file.")


def generate_passport(user_id: Optional[str] = None, name: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a demo cultural passport with realistic data
    
    Args:
        user_id: Optional user ID (generated if not provided)
        name: Optional user name (generated if not provided)
        
    Returns:
        Dictionary with passport data
    """
    # Generate user ID if not provided
    if not user_id:
        user_id = f"usr_{random.randint(1000, 9999)}"
    
    # Generate name if not provided
    if not name:
        first_names = ["João", "Maria", "Pedro", "Ana", "Lucas", "Juliana", "Carlos", "Beatriz"]
        last_names = ["Silva", "Santos", "Oliveira", "Costa", "Rodrigues", "Fernandes"]
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    # Generate birth date (between 1970 and 2000)
    birth_year = random.randint(1970, 2000)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    birth_date = f"{birth_year:04d}-{birth_month:02d}-{birth_day:02d}"
    
    # Generate vibrational signature (sample Solfeggio frequencies)
    solfeggio_frequencies = [174, 285, 396, 417, 528, 639, 741, 852, 963]
    vibrational_signature = random.sample(solfeggio_frequencies, 3)
    vibrational_signature.sort()
    
    # Generate archetypes
    available_archetypes = [
        "Explorer", "Creator", "Hero", "Caregiver", "Sage",
        "Innocent", "Magician", "Rebel", "Lover", "Ruler"
    ]
    archetypes = random.sample(available_archetypes, 2)
    
    # Generate talents
    available_talents = [
        "musical", "analytical", "linguistic", "spatial",
        "kinesthetic", "interpersonal", "intrapersonal", "naturalistic"
    ]
    talents = random.sample(available_talents, 2)
    
    # Generate cultural markers
    cultural_markers = {
        "language": random.choice(["pt-BR", "en-US", "es-ES"]),
        "region": random.choice(["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"]),
        "interests": random.sample(
            ["music", "technology", "nature", "art", "sports", "philosophy", "science"],
            3
        ),
        "values": random.sample(
            ["creativity", "connection", "growth", "freedom", "wisdom", "harmony"],
            2
        )
    }
    
    # Build passport
    passport = {
        "user_id": user_id,
        "name": name,
        "birth_date": birth_date,
        "vibrational_signature": vibrational_signature,
        "archetypes": archetypes,
        "talents": talents,
        "cultural_markers": cultural_markers
    }
    
    return passport


def save_passport_to_file(passport: Dict[str, Any], output_file: str = "passport.json"):
    """
    Save passport to JSON file
    
    Args:
        passport: Passport dictionary
        output_file: Output file path
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(passport, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Passport saved to: {output_file}")


def create_passport_via_api(passport: Dict[str, Any], api_url: str = "http://localhost:8000") -> bool:
    """
    Create passport via API endpoint
    
    Args:
        passport: Passport dictionary
        api_url: Base API URL
        
    Returns:
        True if successful, False otherwise
    """
    if not REQUESTS_AVAILABLE:
        print("❌ Cannot call API: 'requests' library not available")
        return False
    
    try:
        response = requests.post(
            f"{api_url}/passport",
            json=passport,
            timeout=10
        )
        
        if response.status_code == 201:
            print(f"✅ Passport created via API successfully!")
            print(f"   Response: {response.json()}")
            return True
        elif response.status_code == 409:
            print(f"⚠️  Passport already exists for user_id: {passport['user_id']}")
            return False
        else:
            print(f"❌ API request failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to API at {api_url}")
        print("   Make sure the backend server is running:")
        print("   cd modules/cultural-world/backend")
        print("   uvicorn app.main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error calling API: {str(e)}")
        return False


def display_passport(passport: Dict[str, Any]):
    """
    Display passport in a formatted way
    
    Args:
        passport: Passport dictionary
    """
    print("\n" + "="*60)
    print("🌀 CULTURAL PASSPORT 🌀")
    print("="*60)
    print(f"User ID: {passport['user_id']}")
    print(f"Name: {passport['name']}")
    print(f"Birth Date: {passport['birth_date']}")
    print(f"\n🎵 Vibrational Signature: {passport['vibrational_signature']} Hz")
    print(f"🎭 Archetypes: {', '.join(passport['archetypes'])}")
    print(f"🌟 Talents: {', '.join(passport['talents'])}")
    print(f"\n🌍 Cultural Markers:")
    for key, value in passport['cultural_markers'].items():
        print(f"   {key}: {value}")
    print("="*60 + "\n")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Generate and optionally create a demo cultural passport"
    )
    parser.add_argument(
        "--api-url",
        default="http://localhost:8000",
        help="Base URL of the Cultural World API (default: http://localhost:8000)"
    )
    parser.add_argument(
        "--output",
        default="passport.json",
        help="Output JSON file path (default: passport.json)"
    )
    parser.add_argument(
        "--user-id",
        help="Custom user ID (optional, will be generated if not provided)"
    )
    parser.add_argument(
        "--name",
        help="Custom user name (optional, will be generated if not provided)"
    )
    parser.add_argument(
        "--no-api",
        action="store_true",
        help="Skip API call and only save to file"
    )
    
    args = parser.parse_args()
    
    print("🌀 Cultural World Adaptive Nexus - Passport Generator 🌀\n")
    
    # Generate passport
    print("Generating demo passport...")
    passport = generate_passport(user_id=args.user_id, name=args.name)
    
    # Display passport
    display_passport(passport)
    
    # Save to file
    save_passport_to_file(passport, args.output)
    
    # Optionally create via API
    if not args.no_api:
        print(f"\nAttempting to create passport via API at {args.api_url}...")
        create_passport_via_api(passport, args.api_url)
    
    print("\n✨ Done! ✨")
    print("\nNext steps:")
    print("1. Start the backend server if not running:")
    print("   cd modules/cultural-world/backend")
    print("   uvicorn app.main:app --reload")
    print("\n2. Test the API:")
    print("   curl http://localhost:8000/docs")
    print("\n3. Run analysis on the passport:")
    print(f"   curl -X GET http://localhost:8000/passport/{passport['user_id']}")


if __name__ == "__main__":
    main()
