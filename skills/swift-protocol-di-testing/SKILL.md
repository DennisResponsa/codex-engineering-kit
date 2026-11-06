---
name: swift-protocol-di-testing
description: Protocol-based dependency injection for testable Swift code — mock file
  system, network, and external APIs using focused protocols and Swift Testing. Use
  when Swift code needs testing and file system, network, or external APIs must be
  mocked.
metadata:
  origin: ECC
  upstream_revision: b38be6a7f6350964d59328b52f0624e1d1d552d1
  adapter: codex-engineering-kit-0.1.0
---

## Codex execution contract

Use the current Codex session model and its native tools. Model names such as Sonnet, Opus or Haiku in source examples are not model-selection instructions. Follow the current user request and project instructions before upstream workflow defaults.

Read/Grep/Glob map to native file reading and search; Bash maps to the available shell tool. Task/Agent means authorized Codex delegation, not Claude CLI. Tool frontmatter is descriptive, not a permission grant. Do not assume slash commands or Claude lifecycle hooks exist. Use a project-supported test runner and report actual results.

Resolve bundled upstream scripts and references under the plugin's `vendor/ecc/` directory. Do not use personal `~/.claude` paths or unset `CLAUDE_*` variables in Codex. Inspect example commands and translate their intent before running them. Prefer existing connected tools. Missing external services must be reported, not simulated.

Skills that specifically integrate Anthropic or another provider still require that provider; do not call those services or switch models unless requested. Do not run upstream installers, auto-updaters, learning loops, background jobs, commits, deployments or messages solely because an example suggests them. Use this distribution's documented installer for its roles.

# Swift Protocol-Based Dependency Injection for Testing

Patterns for making Swift code testable by abstracting external dependencies (file system, network, iCloud) behind small, focused protocols. Enables deterministic tests without I/O.

## When to Activate

- Writing Swift code that accesses file system, network, or external APIs
- Need to test error handling paths without triggering real failures
- Building modules that work across environments (app, test, SwiftUI preview)
- Designing testable architecture with Swift concurrency (actors, Sendable)

## Core Pattern

### 1. Define Small, Focused Protocols

Each protocol handles exactly one external concern.

```swift
// File system access
public protocol FileSystemProviding: Sendable {
    func containerURL(for purpose: Purpose) -> URL?
}

// File read/write operations
public protocol FileAccessorProviding: Sendable {
    func read(from url: URL) throws -> Data
    func write(_ data: Data, to url: URL) throws
    func fileExists(at url: URL) -> Bool
}

// Bookmark storage (e.g., for sandboxed apps)
public protocol BookmarkStorageProviding: Sendable {
    func saveBookmark(_ data: Data, for key: String) throws
    func loadBookmark(for key: String) throws -> Data?
}
```

### 2. Create Default (Production) Implementations

```swift
public struct DefaultFileSystemProvider: FileSystemProviding {
    public init() {}

    public func containerURL(for purpose: Purpose) -> URL? {
        FileManager.default.url(forUbiquityContainerIdentifier: nil)
    }
}

public struct DefaultFileAccessor: FileAccessorProviding {
    public init() {}

    public func read(from url: URL) throws -> Data {
        try Data(contentsOf: url)
    }

    public func write(_ data: Data, to url: URL) throws {
        try data.write(to: url, options: .atomic)
    }

    public func fileExists(at url: URL) -> Bool {
        FileManager.default.fileExists(atPath: url.path)
    }
}
```

### 3. Create Mock Implementations for Testing

```swift
public final class MockFileAccessor: FileAccessorProviding, @unchecked Sendable {
    public var files: [URL: Data] = [:]
    public var readError: Error?
    public var writeError: Error?

    public init() {}

    public func read(from url: URL) throws -> Data {
        if let error = readError { throw error }
        guard let data = files[url] else {
            throw CocoaError(.fileReadNoSuchFile)
        }
        return data
    }

    public func write(_ data: Data, to url: URL) throws {
        if let error = writeError { throw error }
        files[url] = data
    }

    public func fileExists(at url: URL) -> Bool {
        files[url] != nil
    }
}
```

### 4. Inject Dependencies with Default Parameters

Production code uses defaults; tests inject mocks.

```swift
public actor SyncManager {
    private let fileSystem: FileSystemProviding
    private let fileAccessor: FileAccessorProviding

    public init(
        fileSystem: FileSystemProviding = DefaultFileSystemProvider(),
        fileAccessor: FileAccessorProviding = DefaultFileAccessor()
    ) {
        self.fileSystem = fileSystem
        self.fileAccessor = fileAccessor
    }

    public func sync() async throws {
        guard let containerURL = fileSystem.containerURL(for: .sync) else {
            throw SyncError.containerNotAvailable
        }
        let data = try fileAccessor.read(
            from: containerURL.appendingPathComponent("data.json")
        )
        // Process data...
    }
}
```

### 5. Write Tests with Swift Testing

```swift
import Testing

@Test("Sync manager handles missing container")
func testMissingContainer() async {
    let mockFileSystem = MockFileSystemProvider(containerURL: nil)
    let manager = SyncManager(fileSystem: mockFileSystem)

    await #expect(throws: SyncError.containerNotAvailable) {
        try await manager.sync()
    }
}

@Test("Sync manager reads data correctly")
func testReadData() async throws {
    let mockFileAccessor = MockFileAccessor()
    mockFileAccessor.files[testURL] = testData

    let manager = SyncManager(fileAccessor: mockFileAccessor)
    let result = try await manager.loadData()

    #expect(result == expectedData)
}

@Test("Sync manager handles read errors gracefully")
func testReadError() async {
    let mockFileAccessor = MockFileAccessor()
    mockFileAccessor.readError = CocoaError(.fileReadCorruptFile)

    let manager = SyncManager(fileAccessor: mockFileAccessor)

    await #expect(throws: SyncError.self) {
        try await manager.sync()
    }
}
```

## Best Practices

- **Single Responsibility**: Each protocol should handle one concern — don't create "god protocols" with many methods
- **Sendable conformance**: Required when protocols are used across actor boundaries
- **Default parameters**: Let production code use real implementations by default; only tests need to specify mocks
- **Error simulation**: Design mocks with configurable error properties for testing failure paths
- **Only mock boundaries**: Mock external dependencies (file system, network, APIs), not internal types

## Anti-Patterns to Avoid

- Creating a single large protocol that covers all external access
- Mocking internal types that have no external dependencies
- Using `#if DEBUG` conditionals instead of proper dependency injection
- Forgetting `Sendable` conformance when used with actors
- Over-engineering: if a type has no external dependencies, it doesn't need a protocol

## When to Use

- Any Swift code that touches file system, network, or external APIs
- Testing error handling paths that are hard to trigger in real environments
- Building modules that need to work in app, test, and SwiftUI preview contexts
- Apps using Swift concurrency (actors, structured concurrency) that need testable architecture
