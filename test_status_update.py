"""
Test script to verify send_status_to_db function works correctly
Run this after starting the Internal API service
"""
import asyncio
from Workers.send_status import send_status_to_db


async def test_send_status():
    """Test the status update function"""
    
    # Test case 1: Update status for an existing task
    print("Testing status update...")
    try:
        await send_status_to_db(id=1, status="Testing status update")
        print("✅ Status update successful!")
    except Exception as e:
        print(f"❌ Status update failed: {e}")
    
    # Test case 2: Update with different statuses
    statuses = [
        "Collecting Meta Data",
        "Collected Meta",
        "Processed metadata",
        "Dispatched metadata"
    ]
    
    for status in statuses:
        try:
            await send_status_to_db(id=1, status=status)
            print(f"✅ Updated to: {status}")
        except Exception as e:
            print(f"❌ Failed for '{status}': {e}")
    
    print("\nTest completed!")


if __name__ == "__main__":
    print("=" * 60)
    print("Testing send_status_to_db function")
    print("=" * 60)
    print("\nMake sure the Internal API is running on port 8001")
    print("And that a task with id=1 exists in the database\n")
    
    asyncio.run(test_send_status())
