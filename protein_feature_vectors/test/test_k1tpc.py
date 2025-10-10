#!/usr/bin/env python3
import sys
import os

# Add the protein_feature_vectors directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'protein_feature_vectors'))

from calculator import Calculator

# Test the K1TPC implementation
calc = Calculator(verbose=True)

# Test with the example sequence MLKTSSPC
test_seqs = {
    "test_seq": "MLKTSSPC"
}

print("Testing K1TPC with sequence: MLKTSSPC")
print("Expected 1-spaced tripeptides:")
print("- Positions 0,2,4: M,K,S -> MKS")
print("- Positions 1,3,5: L,T,S -> LTS") 
print("- Positions 2,4,6: K,S,P -> KSP")
print("- Positions 3,5,7: T,S,C -> TSC")
print()

try:
    calc.get_feature_vectors("K1TPC", pdict=test_seqs)
    print("K1TPC calculation completed successfully!")
    print(f"Shape of result: {calc.encodings.shape}")
    print(f"Vector length: {calc.encodings.shape[1]}")
    
    # Check if we got the expected 8000 features
    if calc.encodings.shape[1] == 8000:
        print("✓ Correct vector length of 8000")
    else:
        print(f"✗ Expected 8000 features, got {calc.encodings.shape[1]}")
    
    # Display first few non-zero values to verify
    non_zero_cols = calc.encodings.columns[calc.encodings.iloc[0] > 0]
    if len(non_zero_cols) > 0:
        print(f"\nFound {len(non_zero_cols)} non-zero features:")
        for col in non_zero_cols:
            value = calc.encodings.iloc[0][col]
            print(f"  {col}: {value:.6f}")
    else:
        print("No non-zero features found")
        
except Exception as e:
    print(f"Error testing K1TPC: {e}")
    import traceback
    traceback.print_exc()