from zipzip_tree import ZipZipTree, Rank


def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
   bins_space = [0.0]  # 첫 번째 bin으로 시작
    
   for i in range(len(items)):
      item = items[i]
      bin_assigned = False
      
      # 기존 bin들을 순서대로 확인하여 첫 번째로 맞는 bin에 할당
      for j in range(len(bins_space)):
         if bins_space[j] + item <= 1.0:  # 현재 bin에 들어갈 수 있으면
               bins_space[j] += item
               assignment[i] = j
               bin_assigned = True
               break
      
      # 맞는 bin을 못 찾았으면 새 bin 생성
      if not bin_assigned:
         bins_space.append(item)
         assignment[i] = len(bins_space) - 1
   
   # 모든 bin의 남은 공간을 계산
   for bin_space in bins_space:
      free_space.append(1.0 - bin_space)



def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):



   # 원본 아이템의 인덱스를 저장하며 정렬
   indexed_items = list(enumerate(items))
   indexed_items.sort(key=lambda x: x[1], reverse=True)
   
   bins_space = [0.0]  # 첫 번째 bin으로 시작
   
   # 크기 순으로 정렬된 아이템들 처리
   for original_index, item in indexed_items:
       bin_assigned = False
       
       # 기존 bin들을 순서대로 확인
       for j in range(len(bins_space)):
           if bins_space[j] + item <= 1.0:  # 현재 bin에 들어갈 수 있으면
               bins_space[j] += item
               assignment[original_index] = j
               bin_assigned = True
               break
       
       # 맞는 bin을 못 찾았으면 새 bin 생성
       if not bin_assigned:
           bins_space.append(item)
           assignment[original_index] = len(bins_space) - 1
   
   # 모든 bin의 남은 공간을 계산
   for bin_space in bins_space:
       free_space.append(1.0 - bin_space)