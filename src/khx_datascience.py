#!/usr/bin/env python3
"""
KHX Data Science Module - DataFrames & Analysis
"""

import statistics
import json


class KHXDataFrame:
    """Simple DataFrame implementation"""
    
    def __init__(self, data=None):
        self.data = data if data else []
        self.columns = []
        
        if self.data and len(self.data) > 0:
            if isinstance(self.data[0], dict):
                self.columns = list(self.data[0].keys())
        
        print(f"[DataFrame] Created with {len(self.data)} rows")
    
    def head(self, n=5):
        """Get first n rows"""
        return self.data[:n]
    
    def tail(self, n=5):
        """Get last n rows"""
        return self.data[-n:]
    
    def filter(self, condition):
        """Filter rows (simplified)"""
        # In real implementation, would parse condition
        filtered = [row for row in self.data if self._eval_condition(row, condition)]
        return KHXDataFrame(filtered)
    
    def _eval_condition(self, row, condition):
        """Evaluate condition (placeholder)"""
        return True
    
    def group_by(self, column):
        """Group by column"""
        groups = {}
        for row in self.data:
            key = row.get(column)
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        
        print(f"[DataFrame] Grouped by '{column}': {len(groups)} groups")
        return groups
    
    def mean(self, column):
        """Calculate mean of column"""
        values = [row.get(column, 0) for row in self.data if isinstance(row.get(column), (int, float))]
        if values:
            return statistics.mean(values)
        return 0
    
    def sum(self, column):
        """Sum column"""
        values = [row.get(column, 0) for row in self.data if isinstance(row.get(column), (int, float))]
        return sum(values)
    
    def count(self):
        """Count rows"""
        return len(self.data)
    
    def describe(self):
        """Statistical summary"""
        stats = {}
        for col in self.columns:
            values = [row.get(col, 0) for row in self.data if isinstance(row.get(col), (int, float))]
            if values:
                stats[col] = {
                    'count': len(values),
                    'mean': statistics.mean(values),
                    'min': min(values),
                    'max': max(values),
                    'median': statistics.median(values)
                }
        return stats
    
    def to_json(self):
        """Convert to JSON"""
        return json.dumps(self.data)
    
    def to_csv(self, filename):
        """Export to CSV"""
        if not self.data:
            return False
        
        with open(filename, 'w') as f:
            # Header
            f.write(','.join(self.columns) + '\n')
            # Rows
            for row in self.data:
                values = [str(row.get(col, '')) for col in self.columns]
                f.write(','.join(values) + '\n')
        
        print(f"[DataFrame] Exported to {filename}")
        return True


class KHXArray:
    """Numpy-like array"""
    
    def __init__(self, data):
        self.data = data
        self.shape = (len(data),)
        print(f"[Array] Created with shape {self.shape}")
    
    def mean(self):
        """Calculate mean"""
        return statistics.mean(self.data)
    
    def sum(self):
        """Sum all elements"""
        return sum(self.data)
    
    def min(self):
        """Minimum value"""
        return min(self.data)
    
    def max(self):
        """Maximum value"""
        return max(self.data)
    
    def sort(self):
        """Sort array"""
        return KHXArray(sorted(self.data))
    
    def filter(self, condition):
        """Filter elements"""
        filtered = [x for x in self.data if condition(x)]
        return KHXArray(filtered)
    
    def map(self, func):
        """Map function to elements"""
        mapped = [func(x) for x in self.data]
        return KHXArray(mapped)


class KHXPlot:
    """Simple plotting (text-based)"""
    
    @staticmethod
    def bar(data, labels=None):
        """Bar chart (ASCII)"""
        print("\n[Plot] Bar Chart:")
        max_val = max(data) if data else 1
        
        for i, val in enumerate(data):
            label = labels[i] if labels and i < len(labels) else f"Item {i}"
            bar_length = int((val / max_val) * 40)
            bar = '█' * bar_length
            print(f"{label:10} | {bar} {val}")
    
    @staticmethod
    def line(data):
        """Line chart (ASCII)"""
        print("\n[Plot] Line Chart:")
        max_val = max(data) if data else 1
        min_val = min(data) if data else 0
        
        for val in data:
            normalized = int(((val - min_val) / (max_val - min_val)) * 20) if max_val != min_val else 10
            print(' ' * normalized + '●')
    
    @staticmethod
    def histogram(data, bins=10):
        """Histogram"""
        print(f"\n[Plot] Histogram ({bins} bins):")
        if not data:
            return
        
        min_val = min(data)
        max_val = max(data)
        bin_width = (max_val - min_val) / bins
        
        bins_count = [0] * bins
        for val in data:
            bin_idx = min(int((val - min_val) / bin_width), bins - 1)
            bins_count[bin_idx] += 1
        
        KHXPlot.bar(bins_count)


# Global registry
_dataframes = {}
_arrays = {}
_df_counter = 0
_arr_counter = 0


def create_dataframe(data):
    """Create DataFrame"""
    global _df_counter
    df = KHXDataFrame(data)
    df_id = f"df_{_df_counter}"
    _dataframes[df_id] = df
    _df_counter += 1
    return df_id


def get_dataframe(df_id):
    """Get DataFrame"""
    return _dataframes.get(df_id)


def create_array(data):
    """Create Array"""
    global _arr_counter
    arr = KHXArray(data)
    arr_id = f"arr_{_arr_counter}"
    _arrays[arr_id] = arr
    _arr_counter += 1
    return arr_id


def get_array(arr_id):
    """Get Array"""
    return _arrays.get(arr_id)


def read_csv(filename):
    """Read CSV file"""
    try:
        data = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                return create_dataframe([])
            
            headers = lines[0].strip().split(',')
            for line in lines[1:]:
                values = line.strip().split(',')
                row = dict(zip(headers, values))
                data.append(row)
        
        return create_dataframe(data)
    except Exception as e:
        print(f"[CSV] Error reading file: {e}")
        return create_dataframe([])


def plot_bar(data, labels=None):
    """Plot bar chart"""
    KHXPlot.bar(data, labels)


def plot_line(data):
    """Plot line chart"""
    KHXPlot.line(data)


def plot_histogram(data, bins=10):
    """Plot histogram"""
    KHXPlot.histogram(data, bins)
