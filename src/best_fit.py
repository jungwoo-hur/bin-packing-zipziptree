from zipzip_tree import ZipZipTree, Rank

def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    
   # 각 bin의 현재 사용 공간을 추적
    bins_space = [0.0]  # 첫 번째 bin으로 시작
    
    for i in range(len(items)):
        item = items[i]
        best_bin = -1
        min_space = 1.1  # 1보다 큰 값으로 초기화
        
        # 현재 있는 모든 bin을 확인
        for j in range(len(bins_space)):
            remaining = 1.0 - bins_space[j]
            # 현재 아이템이 들어갈 수 있고, 남는 공간이 더 작은 bin을 찾음
            if item <= remaining and remaining < min_space:
                best_bin = j
                min_space = remaining
        
        # 적절한 bin을 찾지 못했다면 새 bin 생성
        if best_bin == -1:
            bins_space.append(item)
            assignment[i] = len(bins_space) - 1
        else:
            bins_space[best_bin] += item
            assignment[i] = best_bin
    
    # 모든 bin의 남은 공간을 계산
    for bin_space in bins_space:
        free_space.append(1.0 - bin_space)

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
   # 원본 아이템의 인덱스를 저장하며 정렬
    indexed_items = list(enumerate(items))
    indexed_items.sort(key=lambda x: x[1], reverse=True)
    
    # 각 bin의 현재 사용 공간을 추적
    bins_space = [0.0]  # 첫 번째 bin으로 시작
    
    # 크기 순으로 정렬된 아이템들 처리
    for original_index, item in indexed_items:
        best_bin = -1
        min_space = 1.1  # 1보다 큰 값으로 초기화
        
        # 현재 있는 모든 bin을 확인
        for j in range(len(bins_space)):
            remaining = 1.0 - bins_space[j]
            # 현재 아이템이 들어갈 수 있고, 남는 공간이 더 작은 bin을 찾음
            if item <= remaining and remaining < min_space:
                best_bin = j
                min_space = remaining
        
        # 적절한 bin을 찾지 못했다면 새 bin 생성
        if best_bin == -1:
            bins_space.append(item)
            assignment[original_index] = len(bins_space) - 1
        else:
            bins_space[best_bin] += item
            assignment[original_index] = best_bin
    
    # 모든 bin의 남은 공간을 계산
    for bin_space in bins_space:
        free_space.append(1.0 - bin_space)