The task: Write a program that implements a cache policy. 
1. LRU
	- Cache manager, has access to the cache and does all accesses. 
	- Keep track of number of elements in cache
	- getter and setter method for all disk accesses. 
	- Use a dictionary to represent the cache. When inserting an element into the cache
		* First check if cacheEntity is already in the cache, if so, access and return. If not
			* Call block device manager to get block of data. 
			* If cache is not full, then insert cacheEntity
			* If cache is full, then figure out which cacheEntity to evict
	- cacheEntity will need
		* Needs key to identify the data
		* Variable to hold the data, suppose data has a wrapper class
		* Time of last access. Setting or getting would update this number
	- cache itself, the dictionary
		* To get, requires indexing into dictionary, modifying time of last access, return data 
		* To set, requires indexing into dictionary, modifying time of last access, return -1 if failed, 1 if success, write back to disk
			
2. MRU
3. Clock

class CacheManager:
	def __init__(self, size=10): # Size in blocks
		self.size = 10
		self.numEntries = 0
		self.cache = {}
		self.currTime = 0
		self.blockManager = BlockDeviceManager()

	def get(self, idNum):
		if idNum in cache:
			cache[idNum].setTimeLast(self.currTime)
			self.currTime += 1
			return cache[idNum].getData()
		else:
			block = self.blockManager.getBlock(idNum)
			cacheEntry = CacheEntity(self.currTime,block)
			self.currTime += 1
			if numEntries >= self.size: # need to find cacheEntry to evict
				temp = min(self.cache.values()) 
				res = [key for key in self.cache if self.cache[key] == temp] 
				keyToEvict = res[0]
				if self.cache[keyToEvict].isDirty():
					self.blockManager.wroteBlock(keyToEvict,self.cache[keyToEvict])
				del self.cache[keyToEvict]
				self.numEntries -= 1
			self.cache[idNum] = cacheEntry
			self.numEntries += 1
			return block

	def set(self, idNum, data):
		cacheEntry = self.get(idNum)
		cacheEntry.setData(data)
		# self.blockManager.wroteBlockId(idNum,self.cache[idNum])

	def flush(self): # Flush all values to disk upon ending the caching protocol
		pass

class CacheEntity:
	def __init__(self, timeLast, data):
		self.timeLast = timeLast
		self.data = data
		self.dirty = False

	def getTimeLast(self):
		return self.timeLast

	def getData(self):
		return self.data 

	def setData(self, data):
		self.data = data 
		self.dirty = True

	def setTimeLast(self, time):
		self.timeLast = time

	def isDirty(self):
		return self.dirty

class BlockDeviceManager:
	class Block:
		def __init__(self, idNum, blockSize = 4):
			self.blockSize = blockSize
			self.data = [0 for _ in range(self.blockSize)]
			self.idNum = idNum

	def __init__(self, blockSize = 4, blockCapacity = 10):
		self.blockSize = blockSize
		self.blockCapacity = blockCapacity
		self.disk = [Block(i, blockSize) for i in range(self.blockCapacity)]

	def getBlock(self, idNum): # Input verification
		return self.disk[idNum]

	def writeBlock(self, idNum, data):
		self.disk[idNum] = data 